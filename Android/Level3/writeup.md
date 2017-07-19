### Do we need a Android device?
No!

### Running the application
I don't have any android devices, but I did try the IOS challenges and figured I might be able to do some work purely on the binaries.

### Unpacking the APK
I decompiled the APK using JADX: https://github.com/skylot/jadx

```shell
jadx-gui ~/Downloads/ctfone-490954d49dd51911bc730d8161541cf13e7416f9.apk
```

### Examining the code
At first it is unclear where to look for the flag. The solution for the IOS level 3 was based on a HTTP header. While browsing throught the code the following class shoudl be noticed.

```java
package com.h1702ctf.ctfone;

import java.io.IOException;
import okhttp3.CertificatePinner;
import okhttp3.OkHttpClient.Builder;
import okhttp3.Request;

public class Requestor {
    private static String sHostname = "h1702ctf.com";
    private static String sUrl = "https://h1702ctf.com/About";

    public static native String hName();

    public static native String hVal();

    public static void request() {
        try {
            new Builder().certificatePinner(new CertificatePinner.Builder().add(sHostname, "sha256/8yKUtMm6FtEse2v0yDMtT0hKagvpKSWHpnufb1JP5g8=").add(sHostname, "sha256/YLh1dUR9y6Kja30RrAn7JKnbQG/uEtLMkBgFF2Fuihg=").add(sHostname, "sha256/Vjs8r4z+80wjNcr1YKepWQboSIRi63WsWXhIMN+eWys=").build()).build().newCall(new Request.Builder().url(sUrl).addHeader(hName(), hVal()).build()).execute();
        } catch (IOException e) {
        }
    }
}
```

The `hName` and `hVal` are external function calls. These functions are implemented in the library `ctfone-490954d49dd51911bc730d8161541cf13e7416f9/lib/armeabi-v7a/libnative-lib.so`.

### Decompilation
For decompilation of the binary I used Hopper 3. The `hVal` function is easy to spot and can be decompiled to the following pseudo code.

```c
void Java_com_h1702ctf_ctfone_Requestor_hVal(int arg0) {
    r0 = arg0;
    if (*0xc0ca == 0x0) {
            r1 = 0x0;
            do {
                    *(0xc0ca + r1) = *(0xc012 + r1) ^ 0x3e;
                    r1 = r1 + 0x1;
            } while (r1 != 0x48);
    }
    (*(*r0 + 0x29c))();
    return;
}
``` 

The above code is quite easy to follow. It is a while loop with a counter stored in `r1`. An char array is being read from `0xc012`. The total length is 72 bytes (0x48). The contents of these bytes ix XOR-ed against `0x3e`.

The contents of 0xc012 in the binary is: `\x68\x0f\x6c\x7d\x6c\x0c\x6f\x47\x6b\x66\x5a\x71\x68\x79\x6c\x71\x68\x53\x4e\x50\x5a\x0f\x52\x4d\x69\x6a\x68\x55\x68\x0f\x74\x67\x6a\x68\x5a\x4d\x6a\x55\x0e\x49\x5d\x79\x0f\x6b\x5f\x55\x4e\x48\x64\x68\x6b\x46\x70\x52\x6c\x4f\x5c\x7b\x6c\x5f\x5b\x54\x7f\x0b\x6f\x0c\x5d\x07\x6e\x6f\x51\x03`

We can do the exact same thing in python.

### Python to the rescue

The following python script will decode the XOR 'encrypted' value.

```python
data = "\x68\x0f\x6c\x7d\x6c\x0c\x6f\x47\x6b\x66\x5a\x71\x68\x79\x6c\x71\x68\x53\x4e\x50\x5a\x0f\x52\x4d\x69\x6a\x68\x55\x68\x0f\x74\x67\x6a\x68\x5a\x4d\x6a\x55\x0e\x49\x5d\x79\x0f\x6b\x5f\x55\x4e\x48\x64\x68\x6b\x46\x70\x52\x6c\x4f\x5c\x7b\x6c\x5f\x5b\x54\x7f\x0b\x6f\x0c\x5d\x07\x6e\x6f\x51\x03"
xorchr = "\x3e"

out= ""
for letter in data:
    out += (chr(ord(letter) ^ ord(xorchr)))
```

After reading the value it seems to be base64 encoded. After decoding the next value, it seems another base64 encoded value (with a \n at the end). How long will this go on? Lets code it away.

The full script:

```python
import base64

# Address in binary:
data = "\x68\x0f\x6c\x7d\x6c\x0c\x6f\x47\x6b\x66\x5a\x71\x68\x79\x6c\x71\x68\x53\x4e\x50\x5a\x0f\x52\x4d\x69\x6a\x68\x55\x68\x0f\x74\x67\x6a\x68\x5a\x4d\x6a\x55\x0e\x49\x5d\x79\x0f\x6b\x5f\x55\x4e\x48\x64\x68\x6b\x46\x70\x52\x6c\x4f\x5c\x7b\x6c\x5f\x5b\x54\x7f\x0b\x6f\x0c\x5d\x07\x6e\x6f\x51\x03"
xorchr = "\x3e"

out= ""
for letter in data:
    out += (chr(ord(letter) ^ ord(xorchr)))

while True:
    try:
        out = base64.b64decode(out).strip(b'\n')
        print(out.decode('ascii'))
    except:
        break
```

Output:

```
WTBGd2QwNTdNVjgwYlY5dWRXMWlNM0pmTjJoeU16TjlDZz09Cg==
Y0Fwd057MV80bV9udW1iM3JfN2hyMzN9Cg==
cApwN{1_4m_numb3r_7hr33}
```

Ahhh there it is :)
