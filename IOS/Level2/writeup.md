### Do we need a jailbreak?
No!

### Running the application
To run these IPA files I use Appmon (https://github.com/dpnishant/appmon), or I manually sign the applications. Appmon will re-sign (codesign) the application with your developer certificate and sideload Frida. Appmon is a bit of glue for several other utilities like node-applesign and ios-deploy. 

An example of an Appmon deployment, using its ipa_installer.py:
`python ipa_installer.py -ipa ~/Downloads/IntroLevels-727e07e27199b5431fccc16850d67c4fea6596f7.ipa`

Make sure to run Frida on attachment. Also make sure all Appmon requirements are met, like having a correct provisioning profile for the iPhone/iPad. Read the Appmon docs!

`frida -U Gadget`

### Look at the application
There are no messages on the console. We can see a He Man background, some label, a small txt box, a Done button and a larger textbox. Note that I am doing this on a iPhone 4S. The application does not scale correctly, therefore I can not read the bottom larger textbox. No worries though, we can use Frida.

In the Frida console:
`ObjC.classes.UIWindow.keyWindow().recursiveDescription().toString()`

Output:
```
"<UIWindow: 0x1667e520; frame = (0 0; 320 480); gestureRecognizers = <NSArray: 0x16681870>; layer = <UIWindowLayer: 0x16680c10>>
   | <UILayoutContainerView: 0x1659c390; frame = (0 0; 320 480); autoresize = W+H; layer = <CALayer: 0x1659c960>>
   |    | <UITransitionView: 0x1659cdf0; frame = (0 0; 320 480); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x165711d0>>
   |    |    | <UIViewControllerWrapperView: 0x1657b820; frame = (0 0; 320 480); autoresize = W+H; layer = <CALayer: 0x1665b1a0>>
   |    |    |    | <UIView: 0x16594850; frame = (0 0; 320 480); autoresize = W+H; layer = <CALayer: 0x16594590>>
   |    |    |    |    | <UIImageView: 0x1659c990; frame = (-161 0; 595 618); autoresize = RM+BM; userInteractionEnabled = NO; layer = <CALayer: 0x1659ca70>>
   |    |    |    |    | <UILabel: 0x16596980; frame = (130 277; 114 65); text = 'Level 1'; opaque = NO; autoresize = RM+BM; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x1656d470>>
   |    |    |    |    | <_UILayoutGuide: 0x16582240; frame = (0 0; 0 20); hidden = YES; layer = <CALayer: 0x16582a60>>
   |    |    |    |    | <_UILayoutGuide: 0x1659d960; frame = (0 431; 0 49); hidden = YES; layer = <CALayer: 0x1659da30>>
   |    | <UITabBar: 0x16675a60; frame = (0 431; 320 49); autoresize = W+TM; layer = <CALayer: 0x16671aa0>>
   |    |    | <_UITabBarBackgroundView: 0x1657bae0; frame = (0 0; 320 49); autoresize = W; userInteractionEnabled = NO; layer = <CALayer: 0x16578270>>
   |    |    |    | <_UIBackdropView: 0x165a1c20; frame = (0 0; 320 49); opaque = NO; autoresize = W+H; userInteractionEnabled = NO; layer = <_UIBackdropViewLayer: 0x165a1fb0>>
   |    |    |    |    | <_UIBackdropEffectView: 0x165a2a30; frame = (0 0; 320 49); clipsToBounds = YES; opaque = NO; autoresize = W+H; userInteractionEnabled = NO; layer = <CABackdropLayer: 0x165a2cf0>>
   |    |    |    |    | <UIView: 0x165a3450; frame = (0 0; 320 49); hidden = YES; opaque = NO; autoresize = W+H; userInteractionEnabled = NO; layer = <CALayer: 0x165a3510>>
   |    |    | <UITabBarButton: 0x1666ae20; frame = (2 1; 76 48); opaque = NO; layer = <CALayer: 0x16593ed0>>
   |    |    |    | <UITabBarSwappableImageView: 0x165945c0; frame = (23 3; 30 30); opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x16594820>>
   |    |    |    | <UITabBarButtonLabel: 0x1667b0f0; frame = (21.5 35; 33 12); text = 'Level 1'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x16672f90>>
   |    |    | <UITabBarButton: 0x16597190; frame = (82 1; 76 48); opaque = NO; layer = <CALayer: 0x165974c0>>
   |    |    |    | <UITabBarSwappableImageView: 0x16597730; frame = (22.5 3; 30 30); opaque = NO; userInteractionEnabled = NO; tintColor = UIDeviceWhiteColorSpace 0.572549 1; layer = <CALayer: 0x16597650>>
   |    |    |    | <UITabBarButtonLabel: 0x165972d0; frame = (20.5 35; 34.5 12); text = 'Level 2'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x165739a0>>
   |    |    | <UITabBarButton: 0x16597d10; frame = (162 1; 76 48); opaque = NO; layer = <CALayer: 0x16598160>>
   |    |    |    | <UITabBarSwappableImageView: 0x16598370; frame = (22.5 3; 30 30); opaque = NO; userInteractionEnabled = NO; tintColor = UIDeviceWhiteColorSpace 0.572549 1; layer = <CALayer: 0x165982c0>>
   |    |    |    | <UITabBarButtonLabel: 0x16597f90; frame = (20.5 35; 34.5 12); text = 'Level 3'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x16597e70>>
   |    |    | <UITabBarButton: 0x16598b60; frame = (242 1; 76 48); opaque = NO; layer = <CALayer: 0x16598dd0>>
   |    |    |    | <UITabBarSwappableImageView: 0x16598fb0; frame = (23 3; 30 30); opaque = NO; userInteractionEnabled = NO; tintColor = UIDeviceWhiteColorSpace 0.572549 1; layer = <CALayer: 0x16598f60>>
   |    |    |    | <UITabBarButtonLabel: 0x16598ca0; frame = (20.5 35; 35 12); text = 'Level 4'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x16598570>>
   |    |    | <UIImageView: 0x165a3c30; frame = (0 -0.5; 320 0.5); autoresize = W; userInteractionEnabled = NO; layer = <CALayer: 0x165a3d10>>"
[USB::iPhone 4S::Gadget]-> ObjC.classes.UIWindow.keyWindow().recursiveDescription().toString();
"<UIWindow: 0x1667e520; frame = (0 0; 320 480); gestureRecognizers = <NSArray: 0x16681870>; layer = <UIWindowLayer: 0x16680c10>>
   | <UILayoutContainerView: 0x1659c390; frame = (0 0; 320 480); autoresize = W+H; layer = <CALayer: 0x1659c960>>
   |    | <UITransitionView: 0x1659cdf0; frame = (0 0; 320 480); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x165711d0>>
   |    |    | <UIViewControllerWrapperView: 0x165b85c0; frame = (0 0; 320 480); autoresize = W+H; layer = <CALayer: 0x1659f700>>
   |    |    |    | <UIView: 0x165a3e50; frame = (0 0; 320 480); autoresize = W+H; gestureRecognizers = <NSArray: 0x165b07e0>; layer = <CALayer: 0x165b8270>>
   |    |    |    |    | <UIImageView: 0x165b6310; frame = (-268 1; 804 617); autoresize = RM+BM; userInteractionEnabled = NO; layer = <CALayer: 0x165b6250>>
   |    |    |    |    | <UITextField: 0x16679470; frame = (82 337; 162 30); text = ''; clipsToBounds = YES; opaque = NO; autoresize = RM+BM; gestureRecognizers = <NSArray: 0x165c0de0>; layer = <CALayer: 0x1666df70>>
   |    |    |    |    |    | <_UITextFieldRoundedRectBackgroundViewNeue: 0x165afa40; frame = (0 0; 162 30); opaque = NO; autoresize = W+H; userInteractionEnabled = NO; layer = <CALayer: 0x165afc50>>
   |    |    |    |    | <UILabel: 0x165a3890; frame = (82 300; 210 21); text = 'HEYYEYAAEYAAAEYAEYAA'; opaque = NO; autoresize = RM+BM; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x165ae5b0>>
   |    |    |    |    | <UILabel: 0x1659f040; frame = (125 20; 125 43); text = 'Level 2'; opaque = NO; autoresize = RM+BM; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x1659f150>>
   |    |    |    |    | <UIButton: 0x165ae270; frame = (257 337; 37 30); opaque = NO; autoresize = RM+BM; layer = <CALayer: 0x165ae580>>
   |    |    |    |    |    | <UIButtonLabel: 0x165b6530; frame = (0.5 6; 36.5 18); text = 'Done'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x165bda30>>
   |    |    |    |    | <UITextView: 0x16aed600; frame = (67 424; 240 128); text = 'Learn how to hide your fe...'; clipsToBounds = YES; autoresize = RM+BM; gestureRecognizers = <NSArray: 0x165b4950>; layer = <CALayer: 0x165b0eb0>; contentOffset: {0, 0}; contentSize: {240, 33}>
   |    |    |    |    |    | <<_UITextContainerView: 0x165b7a30; frame = (0 0; 240 33); layer = <_UITextTiledLayer: 0x165b7d20>> minSize = {0, 0}, maxSize = {3.4028235e+38, 3.4028235e+38}, textContainer = <NSTextContainer: 0x165b55f0 size = (240.000000,340282346638528859811704183484516925440.000000); widthTracksTextView = YES; heightTracksTextView = NO>; exclusionPaths = 0x1665a330; lineBreakMode = 0>
   |    |    |    |    |    |    | <_UITileLayer: 0x165a3710> (layer)
   |    |    |    |    |    | <UIImageView: 0x165c2330; frame = (3 122.5; 234 2.5); alpha = 0; opaque = NO; autoresize = TM; userInteractionEnabled = NO; layer = <CALayer: 0x165c2440>>
   |    |    |    |    |    | <UIImageView: 0x165c2880; frame = (234.5 98; 2.5 27); alpha = 0; opaque = NO; autoresize = LM; userInteractionEnabled = NO; layer = <CALayer: 0x165c2960>>
   |    |    |    |    | <_UILayoutGuide: 0x165a0140; frame = (0 0; 0 20); hidden = YES; layer = <CALayer: 0x1659f840>>
   |    |    |    |    | <_UILayoutGuide: 0x165a02c0; frame = (0 431; 0 49); hidden = YES; layer = <CALayer: 0x165a0390>>
   |    | <UITabBar: 0x16675a60; frame = (0 431; 320 49); autoresize = W+TM; layer = <CALayer: 0x16671aa0>>
   |    |    | <_UITabBarBackgroundView: 0x1657bae0; frame = (0 0; 320 49); autoresize = W; userInteractionEnabled = NO; layer = <CALayer: 0x16578270>>
   |    |    |    | <_UIBackdropView: 0x165a1c20; frame = (0 0; 320 49); opaque = NO; autoresize = W+H; userInteractionEnabled = NO; layer = <_UIBackdropViewLayer: 0x165a1fb0>>
   |    |    |    |    | <_UIBackdropEffectView: 0x165a2a30; frame = (0 0; 320 49); clipsToBounds = YES; opaque = NO; autoresize = W+H; userInteractionEnabled = NO; layer = <CABackdropLayer: 0x165a2cf0>>
   |    |    |    |    | <UIView: 0x165a3450; frame = (0 0; 320 49); hidden = YES; opaque = NO; autoresize = W+H; userInteractionEnabled = NO; layer = <CALayer: 0x165a3510>>
   |    |    | <UITabBarButton: 0x1666ae20; frame = (2 1; 76 48); opaque = NO; layer = <CALayer: 0x16593ed0>>
   |    |    |    | <UITabBarSwappableImageView: 0x165945c0; frame = (23 3; 30 30); opaque = NO; userInteractionEnabled = NO; tintColor = UIDeviceWhiteColorSpace 0.572549 1; layer = <CALayer: 0x16594820>>
   |    |    |    | <UITabBarButtonLabel: 0x1667b0f0; frame = (21.5 35; 33 12); text = 'Level 1'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x16672f90>>
   |    |    | <UITabBarButton: 0x16597190; frame = (82 1; 76 48); opaque = NO; layer = <CALayer: 0x165974c0>>
   |    |    |    | <UITabBarSwappableImageView: 0x16597730; frame = (22.5 3; 30 30); opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x16597650>>
   |    |    |    | <UITabBarButtonLabel: 0x165972d0; frame = (20.5 35; 34.5 12); text = 'Level 2'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x165739a0>>
   |    |    | <UITabBarButton: 0x16597d10; frame = (162 1; 76 48); opaque = NO; layer = <CALayer: 0x16598160>>
   |    |    |    | <UITabBarSwappableImageView: 0x16598370; frame = (22.5 3; 30 30); opaque = NO; userInteractionEnabled = NO; tintColor = UIDeviceWhiteColorSpace 0.572549 1; layer = <CALayer: 0x165982c0>>
   |    |    |    | <UITabBarButtonLabel: 0x16597f90; frame = (20.5 35; 34.5 12); text = 'Level 3'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x16597e70>>
   |    |    | <UITabBarButton: 0x16598b60; frame = (242 1; 76 48); opaque = NO; layer = <CALayer: 0x16598dd0>>
   |    |    |    | <UITabBarSwappableImageView: 0x16598fb0; frame = (23 3; 30 30); opaque = NO; userInteractionEnabled = NO; tintColor = UIDeviceWhiteColorSpace 0.572549 1; layer = <CALayer: 0x16598f60>>
   |    |    |    | <UITabBarButtonLabel: 0x16598ca0; frame = (20.5 35; 35 12); text = 'Level 4'; opaque = NO; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x16598570>>
   |    |    | <UIImageView: 0x165a3c30; frame = (0 -0.5; 320 0.5); autoresize = W; userInteractionEnabled = NO; layer = <CALayer: 0x165a3d10>>"
```

Notice this: `<UITextView: 0x16aed600; frame = (67 424; 240 128); text = 'Learn how to hide your fe...'; clipsToBounds = YES; autoresize = RM+BM; gestureRecognizers = <NSArray: 0x165b4950>; layer = <CALayer: 0x165b0eb0>; contentOffset: {0, 0}; contentSize: {240, 33}>`

We can further inspect this object in Frida. We load the object, call the text method and convert it to string.
`ObjC.Object(ptr(0x16aed600)).text().toString()`

output:
`"Learn how to hide your feelings"`

Just typical of CTF's. Some references to He man, but not really anything useful, oh well... lets take a look at the 'Done' button.

### Button attachment
What does the button call you ask? I have no clue, lets find out.

`button = ObjC.Object(ptr(0x165ae270))`

`button.allTargets().toString()`

Output:

```
"{(
    <IntroLevels.Level2ViewController: 0x166743f0>
)}"
```

`button.allControlEvents()`

Output:

```
64
```

Use the information to find the handler method

`button.actionsForTarget_forControlEvent_(ptr(0x166743f0),64).toString()`

Output:

```
"(
    "buttonTouched:"
)"
```

Okay so now we now that pressing the button will trigger IntroLevels.Level2ViewController["buttonTouched:"]

### Decompiling
I use Hopper 3 (and 4) and IDA Pro for decompilation. Use all the tools you can for pseudocode generation. The will differ. For instance; Hopper 4 did not jump to `loc_a930`. In Hopper 3 this is shown as `sub_a930` and you will be able to jump to the correct pseudo code.

Now I used IDA as well to look at pseudo code for the function starting at 0xa930. In IDA PRO we can easily spot this:
`v24 = _TTSfq4gs_s___TFSS37_compareDeterministicUnicodeCollationfSSSi("5b6da8f65476a399050c501e27ab7d91", 32, 0, v19);` as well as this `v24 = _swift_stdlib_memcmp(v19, "5b6da8f65476a399050c501e27ab7d91", 32);`. This instantly has my attention, since it looks like an MD5 hash


### Google for #
Googling for the found hash results in this first hit: https://www.thishash.com/md5/5b6da8f65476a399050c501e27ab7d91/. It tells us the string "424241" results in that MD5 hash. Without even further inspecting the code, I enter this into the first txt box and press Done. There seems to be no result. But wait. Lets check the bottom txt field once more.

`ObjC.Object(ptr(0x16aed600)).text().toString()`

Output:

`"cApwN{0mg_d0es_h3_pr4y}"`

That looks like a flag!