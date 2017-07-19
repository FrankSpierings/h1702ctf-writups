### Do we need a jailbreak?
No!

### Running the application
To run these IPA files I use Appmon (https://github.com/dpnishant/appmon), or I manually sign the applications. Appmon will re-sign (codesign) the application with your developer certificate and sideload Frida. Appmon is a bit of glue for several other utilities like node-applesign and ios-deploy. 

An example of an Appmon deployment, using its ipa_installer.py:
`python ipa_installer.py -ipa ~/Downloads/IntroLevels-727e07e27199b5431fccc16850d67c4fea6596f7.ipa`

Make sure to run Frida on attachment. Also make sure all Appmon requirements are met, like having a correct provisioning profile for the iPhone/iPad. Read the Appmon docs!

`frida -U Gadget`

### Look at the application
Once the application started, you will notice a line in lldb stating the following: `Level 1: The flag isn't in the code!`

### Unpacking the IPA
So we should not look in the code... So lets take a look at the application resources.

`unzip IntroLevels-727e07e27199b5431fccc16850d67c4fea6596f7.ipa`

```
Payload/IntroLevels.app/AppIcon20x20@2x.png
Payload/IntroLevels.app/AppIcon20x20@2x~ipad.png
Payload/IntroLevels.app/AppIcon29x29@2x.png
Payload/IntroLevels.app/AppIcon29x29@3x.png
Payload/IntroLevels.app/AppIcon40x40@2x.png
Payload/IntroLevels.app/AppIcon40x40@3x.png
Payload/IntroLevels.app/AppIcon60x60@2x.png
Payload/IntroLevels.app/AppIcon60x60@3x.png
Payload/IntroLevels.app/Assets.car
Payload/IntroLevels.app/Base.lproj/LaunchScreen.storyboardc/01J-lp-oVM-view-Ze5-6b-2t3.nib
Payload/IntroLevels.app/Base.lproj/LaunchScreen.storyboardc/Info.plist
Payload/IntroLevels.app/Base.lproj/LaunchScreen.storyboardc/UIViewController-01J-lp-oVM.nib
Payload/IntroLevels.app/Base.lproj/Main.storyboardc/8rJ-Kc-sve-view-QS5-Rx-YEW.nib
Payload/IntroLevels.app/Base.lproj/Main.storyboardc/9pv-A4-QxB-view-tsR-hK-woN.nib
Payload/IntroLevels.app/Base.lproj/Main.storyboardc/Info.plist
Payload/IntroLevels.app/Base.lproj/Main.storyboardc/UITabBarController-49e-Tb-3d3.nib
Payload/IntroLevels.app/Base.lproj/Main.storyboardc/kfs-sF-5cJ-view-BGB-Fg-ckV.nib
Payload/IntroLevels.app/Base.lproj/Main.storyboardc/zzW-s0-GtA-view-4wd-jj-EQy.nib
Payload/IntroLevels.app/Frameworks/Alamofire.framework/Alamofire
Payload/IntroLevels.app/Frameworks/Alamofire.framework/Info.plist
Payload/IntroLevels.app/Frameworks/Alamofire.framework/_CodeSignature/CodeResources
Payload/IntroLevels.app/Frameworks/CryptoSwift.framework/CryptoSwift
Payload/IntroLevels.app/Frameworks/CryptoSwift.framework/Info.plist
Payload/IntroLevels.app/Frameworks/CryptoSwift.framework/_CodeSignature/CodeResources
Payload/IntroLevels.app/Frameworks/libswiftCore.dylib
Payload/IntroLevels.app/Frameworks/libswiftCoreGraphics.dylib
Payload/IntroLevels.app/Frameworks/libswiftCoreImage.dylib
Payload/IntroLevels.app/Frameworks/libswiftDarwin.dylib
Payload/IntroLevels.app/Frameworks/libswiftDispatch.dylib
Payload/IntroLevels.app/Frameworks/libswiftFoundation.dylib
Payload/IntroLevels.app/Frameworks/libswiftObjectiveC.dylib
Payload/IntroLevels.app/Frameworks/libswiftQuartzCore.dylib
Payload/IntroLevels.app/Frameworks/libswiftUIKit.dylib
Payload/IntroLevels.app/Info.plist
Payload/IntroLevels.app/IntroLevels
Payload/IntroLevels.app/PkgInfo
Payload/IntroLevels.app/_CodeSignature/CodeResources
Payload/IntroLevels.app/embedded.mobileprovision
Payload/IntroLevels.app/google.cer
```

Working down this list:
- AppIcons: can be viewed in a preview window (through Finder). Not interesting.
- Assets.car: sounds like extra assets. Maybe the backgrounds? Lets have a look at this file :)

`file Payload/IntroLevels.app/Assets.car`

`Payload/IntroLevels.app/Assets.car: Mac OS X bill of materials (BOM) file`

Okay, lets Google for a tool that can do something with this type of file. I don't want to reinvent the wheel at this stage.
I found: https://github.com/steventroughtonsmith/cartool. Lets download & compile (I won't go into detail on howto compile this).

Give the cartool a spin:
```
mkdir /tmp/out
cartool Payload/IntroLevels.app/Assets.car /tmp/out
```

```
Matrix-Morpheus
	Matrix-Morpheus.png
first
	first.png
	first@2x.png
he-man-jon-chu-camp
	he-man-jon-chu-camp.png
hqdefault
	hqdefault.png
lizard
	lizard.png
paper
	paper.png
rock
	rock.png
scissors
	scissors.png
second
	second.png
	second@2x.png
spock
	spock.png
```

Check the extracted files. We will see a file called `Matrix-Morpheus.png`. View this file & find the flag.