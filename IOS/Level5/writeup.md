### Do we need a jailbreak?
No!

### Running the application
To run these IPA files I use Appmon (https://github.com/dpnishant/appmon), or I manually sign the applications. Appmon will re-sign (codesign) the application with your developer certificate and sideload Frida. Appmon is a bit of glue for several other utilities like node-applesign and ios-deploy. 

An example of an Appmon deployment, using its ipa_installer.py:
`python ipa_installer.py -ipa ~/Downloads/Level5-69c2713162cb8f5e9418f8c08f3fa0a1ecb4928d.ipa`

Make sure to run Frida on attachment. Also make sure all Appmon requirements are met, like having a correct provisioning profile for the iPhone/iPad. Read the Appmon docs!

`frida -U Gadget`

### Look at the application
The application shows the following line in the console `Run me on a jailbroken device!`. Well, I don't own a jailbroken device, like some rich hacker. I just have a iPhone 4s. Well lets see if we can hack this anyway :)
The application itself shows a nice animated gif of MC Hammer and a button saying `Hamer time!`. Lets find out what the button does.


### Buttons and wiring
Once again, check how the button is wired.

In the Frida console:
`ObjC.classes.UIWindow.keyWindow().recursiveDescription().toString()`

Output:

```
"<UIWindow: 0x15e42930; frame = (0 0; 320 480); autoresize = W+H; gestureRecognizers = <NSArray: 0x15e40650>; layer = <UIWindowLayer: 0x15e31690>>
   | <UIView: 0x15e4c3f0; frame = (0 0; 320 480); autoresize = W+H; layer = <CALayer: 0x15e4c5c0>>
   |    | <UIImageView: 0x15e4c220; frame = (-4 0; 328 240); opaque = NO; autoresize = RM+BM; userInteractionEnabled = NO; animations = { UIImageAnimation=<CAKeyframeAnimation: 0x15d6fe60>; }; layer = <CALayer: 0x15e4c300>>
   |    | <UIButton: 0x15e4a7e0; frame = (139 318; 97 30); opaque = NO; autoresize = RM+BM; layer = <CALayer: 0x15e4aad0>>
   |    |    | <UIButtonLabel: 0x15d6a3d0; frame = (0 6; 97 18); text = 'Hammer time!'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x15d6a720>>
   |    | <_UILayoutGuide: 0x15e4c620; frame = (0 0; 0 20); hidden = YES; layer = <CALayer: 0x15e4c850>>
   |    | <_UILayoutGuide: 0x15e4ccd0; frame = (0 480; 0 0); hidden = YES; layer = <CALayer: 0x15e4cda0>>"
```

Notice this:
`<UIButton: 0x15e4a7e0; frame = (139 318; 97 30); opaque = NO; autoresize = RM+BM; layer = <CALayer: 0x15e4aad0>>`

We can further inspect this object in Frida. We load the object, call the text method and convert it to string.

`button = ObjC.Object(ptr(0x15e4a7e0))`

`button.allTargets().toString()`

Output:
```
"{(
    <Level5Demo.DemoVC: 0x15d6bd10>
)}"
```

`button.allControlEvents()`

Output:
```
64
```

Use the information to find the handler method

`button.actionsForTarget_forControlEvent_(ptr(0x15d6bd10),64).toString()`

Output:
```
"(
    "hammerTime:"
)"
```

Okay so now we now that pressing the button will trigger Level5Demo.DemoVC["hammerTime:"]

### Decompiling
When we decompile the binary in Hopper 3, it will show that the hammerTime method is at address 0xa4e0. In Hopper 3 pseudo code this doesn't show much information. As mentioned in previous writeups, it is a good idea to try other decompilers. Lets have a look at that address in IDA Pro. The following pseudo code is generated.

```
int __fastcall sub_A4E0(int a1, int a2, __objc2_prot *a3)
{
  __objc2_prot *v3; // r5@1
  int v4; // r4@1
  int v5; // r0@3
  int v6; // r0@4
  __objc2_prot *v8; // [sp+0h] [bp-18h]@2
  int v9; // [sp+Ch] [bp-Ch]@2

  v3 = a3;
  v4 = a1;
  if ( a3 )
  {
    v9 = swift_getObjectType(a3);
    v8 = v3;
  }
  else
  {
    v5 = dword_15E10;
    if ( !dword_15E10 )
    {
      v6 = dword_15E14;
      if ( !dword_15E14 )
      {
        v8 = &OBJC_PROTOCOL____TtPs9AnyObject_;
        v6 = sub_BB90(1, &v8);
        __dmb();
        dword_15E14 = v6;
      }
      v5 = _TMaSq(v6);
      __dmb();
      dword_15E10 = v5;
    }
    v9 = v5;
    v8 = 0;
  }
  objc_retain(v4);
  swift_unknownRetain(v3);
  sub_A180(&v8, v4);
  return objc_release(v4);
}
```

Notice sub_A180? Lets have a look. It shows lines like: 

```
  v2 = a1;
  v3 = a2;
  v4 = (void *)objc_allocWithZone(&OBJC_CLASS___KeychainThing);
  v5 = objc_msgSend(v4, "init");
  v6 = _TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSString("setmeinurkeychain", 17, 0);
  v7 = v6;
  v8 = objc_msgSend(v5, "searchKeychainCopyMatching:", v6);
  if ( !objc_retainAutoreleasedReturnValue(v8) )
  {
    v33 = objc_release(v7);
    nullsub_1(v33);
    __und(0xFDEEu);
  }
```

As well as:

```
  v2 = a1;
  v3 = a2;
  v4 = (void *)objc_allocWithZone(&OBJC_CLASS___KeychainThing);
  v5 = objc_msgSend(v4, "init");
  v6 = _TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSString("setmeinurkeychain", 17, 0);
  v7 = v6;
  v8 = objc_msgSend(v5, "searchKeychainCopyMatching:", v6);
  if ( !objc_retainAutoreleasedReturnValue(v8) )
  {
    v33 = objc_release(v7);
    nullsub_1(v33);
    __und(0xFDEEu);
  }
```

Also at the bottom of the function a new ViewController seems to be loaded... interesting.

```
LABEL_11:
  sub_8B0E(nullsub_1);
  sub_8A08(nullsub_1);
  sub_8C2E(nullsub_1);
  sub_8B5C(nullsub_1);
  v23 = _TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSString("Main", 4, 0);
  v24 = (void *)sub_9500(&OBJC_CLASS___UIStoryboard);
  v25 = objc_msgSend(v24, "storyboardWithName:bundle:", v23, 0, v34);
  v26 = (void *)objc_retainAutoreleasedReturnValue(v25);
  objc_release(v23);
  v27 = _TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSString("viewOfViewsController", 21, 0);
  v28 = v27;
  v29 = objc_msgSend(v26, "instantiateViewControllerWithIdentifier:", v27);
  v30 = objc_retainAutoreleasedReturnValue(v29);
  objc_release(v28);
  objc_retain(v36);
  v31 = _TF10ObjectiveC22_convertBoolToObjCBoolFSbVS_8ObjCBool(1);
  objc_msgSend(v36, "presentViewController:animated:completion:", v30, v31, 0);
  sub_BD38(v9);
  objc_release(v14);
  objc_release(v36);
  objc_release(v30);
  objc_release(v26);
  objc_release(v35);
```

With a bit of guess work we can speculate about the working. It checks if a certain keychain item contains a specific value. If that all checks out, it will show us a new screen. So how do we get this information in the keychain? Lets take a look at that `KeychainThing` class with Frida.

 `ObjC.classes.KeychainThing.$ownMethods`

Output:

```
[
    "- newSearchDictionary:",
    "- searchKeychainCopyMatching:",
    "- createKeychainValue:forIdentifier:"
]
```

We might try to use this object to inject an item in the keychain. Who needs a jailbroken phone :) ?

Since these methods are instance methods we first need to allocate space for the KeychainThing object and then initialize it. Next we can call its method. This code comes from some experience and a couple of hours tinkering. Thats what you need if you don't have talent.... time ;)

In Frida we will:

```
k = ObjC.classes.KeychainThing
k = k.alloc()
k = k.init()
k.createKeychainValue_forIdentifier_("youdidathing","setmeinurkeychain")
```

Lets check if it worked through Frida:

```
result = k.searchKeychainCopyMatching_("setmeinurkeychain").bytes()
hexdump(result)
```

Partial output:
```
"           0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
00000000  79 6f 75 64 69 64 61 74 68 69 6e 67 00 00 00 00  youdidathing....
00000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000020  00 00 0a 80 00 00 00 00 00 4d d9 34 60 4b d9 34  .........M.4`K.4
00000030  d0 4c d9 34 1c 4c d9 34 94 6c b2 36 48 34 56 37  .L.4.L.4.l.6H4V7
00000040  78 67 dc 25 00 00 00 00 00 00 00 00 00 00 00 00  xg.%............
00000050  00 00 0a 80 07 00 00 00 28 4c d9 34 f0 4b d9 34  ........(L.4.K.4
00000060  00 00 00 00 1c 4c d9 34 80 6c b2 36 5c 34 56 37  .....L.4.l.6\4V7
```

Well that seems to work. Lets press the button in the app now. 

Yesssss! The app now shows a grid view containing hard to read letters, which spell:

`cApwN{i_guess_you_can_touch_this}`
