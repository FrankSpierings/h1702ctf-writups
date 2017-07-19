### Do we need a jailbreak?
No!

### Running the application
To run these IPA files I use Appmon (https://github.com/dpnishant/appmon), or I manually sign the applications. Appmon will re-sign (codesign) the application with your developer certificate and sideload Frida. Appmon is a bit of glue for several other utilities like node-applesign and ios-deploy. 

An example of an Appmon deployment, using its ipa_installer.py:
`python ipa_installer.py -ipa ~/Downloads/IntroLevels-727e07e27199b5431fccc16850d67c4fea6596f7.ipa`

Make sure to run Frida on attachment. Also make sure all Appmon requirements are met, like having a correct provisioning profile for the iPhone/iPad. Read the Appmon docs!

`frida -U Gadget`

### Look at the application
There are no messages on the console. We can see a couple of images with different signs. No matter what we press, the application tells us we failed and we will be reported as losers. Thanks App! Really helpful ;)

### Buttons and wiring
The images are not directly buttons, so I decide to just open up the application in Hopper 3 this time.

### Decompile
Looking at all the procedures containing `Level3` will show a lot of methods. There is a method called `reportBeingALoser`. After being called a loser so many times during my button presses, I want to know what this actually does. The pseudo code in Hopper 3, shows a call to 0x36cd8 (`sub_36cd8(self)`). Following this function, will show a large amount of lines. There a references to Alamofire in this function. It seems that https://github.com/Alamofire/Alamofire is used for networking. There is a very interesting line in the pseudocode: `[r11 setHTTPAdditionalHeaders:r6];`. Why would it set extra headers? This is not very normal behaviour. So lets inspect the header as it is being send.

### Frida hook setHTTPAdditionalHeaders
Frida is good at hooking stuff, so lets use it. We can use `frida-trace` to do the hard work.

```
cd /tmp
frida-trace -U Gadget -m '-[* setHTTPAdditionalHeaders]'
```

Press a button and click away the loser message.

Output:
```
Instrumenting functions...
-[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:]: Auto-generated handler at "/private/tmp/__handlers__/____NSCFURLSessionConfiguration__99aed094.js"
Started tracing 1 function. Press Ctrl+C to stop.
           /* TID 0xa0b */
  2953 ms  -[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:0x0 ]
  2953 ms  -[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:0x1662ff70 ]
  2954 ms  -[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:0x1662ff70 ]
```

Ah, the function is being called, but we cannot see its value, other than some address. Lets modify the frida-trace script, to show us the goods.

```
vi __handlers__/____NSCFURLSessionConfiguration__99aed094.js
```

Change the OnEnter function to also print the arguments value, using the Memory object.

```
onEnter: function (log, args, state) {
    log("-[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:" + args[2] + " ]");
    log(ObjC.Object(args[2]).toString())
},
```

Lets repeat the frida-trace.

```
cd /tmp
frida-trace -U Gadget -m '-[* setHTTPAdditionalHeaders]'
```

Do the button pressing again...

Output:
```
Instrumenting functions...
-[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:]: Loaded handler at "/private/tmp/__handlers__/____NSCFURLSessionConfiguration__99aed094.js"
Started tracing 1 function. Press Ctrl+C to stop.
{'type': 'error', 'columnNumber': 1, 'fileName': 'objc.js', 'stack': 'TypeError: undefined not callable\n    at [anon] (duk_js_call.c:842)\n    at frida/node_modules/frida-objc/index.js:433\n    at input:24\n    at call (native)\n    at invokeCallback (tracer.js:33)\n    at tracer.js:39', 'lineNumber': 1399, 'description': 'TypeError: undefined not callable'}
           /* TID 0xa0b */
  2560 ms  -[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:0x0 ]
  2695 ms  -[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:0x166e7150 ]
  2695 ms  {
    "look at me i am a header" = "cApwN{1m_1n_ur_n00twork_tere3fik}";
}
  2702 ms  -[__NSCFURLSessionConfiguration setHTTPAdditionalHeaders:0x166e7150 ]
  2702 ms  {
    "look at me i am a header" = "cApwN{1m_1n_ur_n00twork_tere3fik}";
}

```

That looks like a flag!

