### Do we need a jailbreak?
No!

### Running the application
To run these IPA files I use Appmon (https://github.com/dpnishant/appmon), or I manually sign the applications. Appmon will re-sign (codesign) the application with your developer certificate and sideload Frida. Appmon is a bit of glue for several other utilities like node-applesign and ios-deploy. 

An example of an Appmon deployment, using its ipa_installer.py:
`python ipa_installer.py -ipa ~/Downloads/IntroLevels-727e07e27199b5431fccc16850d67c4fea6596f7.ipa`

Make sure to run Frida on attachment. Also make sure all Appmon requirements are met, like having a correct provisioning profile for the iPhone/iPad. Read the Appmon docs!

`frida -U Gadget`

### Look at the application
The application shows the following line in the console `Level 4: Find the function to do the thing`, once you navigate to level 4 (button at the bottom). So we need to find a function to do a thing. Lets open up Hopper 3.


### Decompile
If we look for `thing` in the procedures, it will show `+[ZhuLi doTheThing:flag2:flag3]`. This means there is a class `ZhuLi` with a class method (similar to 'static'). So we do not need to instantiate the ZhuLi class. We could just call the method with the correct variables.

Looking at the pseudo code, it shows the following prototype: `void * +[ZhuLi doTheThing:flag2:flag3:](void * self, void * _cmd, void * arg2, void * arg3, void * ret_addr)`. To be honest, I first figured it needed the following arguments: flag2, flag3 and some return address. After trying that to work I just simply tried the following in Frida.

`ObjC.classes.ZhuLi.doTheThing_flag2_flag3_("","","").toString()`

Output:
`"846317cc0fa8487912baadea1d9d7cf3476bf19a18beae39c4c55e15"`

Changing the input:

`ObjC.classes.ZhuLi.doTheThing_flag2_flag3_("a","","").toString()`

Output:

`"07645b07b7a2933848bd8a5120aed00159cb27fd35d69fe7b52b8722465156c6"`

So the output does change based on its input. Good to know :) . What happens if we insert all three flags in order?

```
flag1 = "cApwN{y0u_are_th3_ch0sen_1}"
flag2 = "cApwN{0mg_d0es_h3_pr4y}"
flag3 = "cApwN{1m_1n_ur_n00twork_tere3fik}"
ObjC.classes.ZhuLi.doTheThing_flag2_flag3_(flag1, flag2, flag3).toString()
```

Output:
`"634170774e7b6630685f7377317a7a6c655f6d795f6e317a7a6c657d"`

Mmmmm that could be Ascii? Lets rip some hex to ascii code from stackoverflow: https://stackoverflow.com/questions/3745666/how-to-convert-from-hex-to-ascii-in-javascript

```
function hex2a(hexx) {
    var hex = hexx.toString();//force conversion
    var str = '';
    for (var i = 0; i < hex.length; i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

hex2a("634170774e7b6630685f7377317a7a6c655f6d795f6e317a7a6c657d")
```

Output:

`"cApwN{f0h_sw1zzle_my_n1zzle}"`

Well.... that seems like the 4th flag :)
