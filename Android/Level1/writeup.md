### Do we need a Android device?
No!

### Running the application
I don't have any android devices, but I did try the IOS challenges and figured I might be able to do some work purely on the binaries.

### Unpacking the APK
I unpacked the APK with apktool: https://ibotpeaches.github.io/Apktool/

Since the IOS level 1 is solved without any code analysis (see my writeup), but simply extracting the correct resource, I figured I should use the same approach. Lets see what assets are in this APK.

```shell
mkdir /tmp/out
apktool d ~/Downloads/ctfone-490954d49dd51911bc730d8161541cf13e7416f9.apk
find . | grep assets
```

Output:

```
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset1
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset10
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset2
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset3
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset4
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset5
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset6
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset7
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset8
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/asset9
./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/tHiS_iS_nOt_tHE_SeCrEt_lEveL_1_fiLE
```

Is it really?

```shell
open ./ctfone-490954d49dd51911bc730d8161541cf13e7416f9/assets/tHiS_iS_nOt_tHE_SeCrEt_lEveL_1_fiLE
```

This will show the flag for level1!