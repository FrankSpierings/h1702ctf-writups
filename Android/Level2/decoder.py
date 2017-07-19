from Crypto.Cipher import AES
import base64

unpad = lambda s : s[0:-ord(s[-1])]

hexct = "ec49822b5417f4dad5d6048804c07f128bb0552673171d078cc2e6b191b4cbaa2d8c5c0bb95e29cee0cb0ea0db961a33ad074d17c3a227d487c85b88487435c97c3f9992b1a3d08f43fc92f416820f95ba463a67b09eb3433fb94ce2d2c5ac25ec49822b5417f4dad5d6048804c07f127c3f9992b1a3d08f43fc92f416820f95ba463a67b09eb3433fb94ce2d2c5ac25069590e37f53bebf7c16b617482a4b8ae151286044c2a8237302612c7d88c8b2ce0eef96ce210effc6a2733a73b371b1d764b219e31def9c556a602e6b236b483469118ed906f6b3abeff55bcdc7e5a00d0d3f3cb085730e3335b7170a03ed91fca1309cccb8078e2a9100cbbeaff61e4be535b1314ecb6fb99b3985c06ae00616288270b1670f7bf609b8c9c3d62e29069590e37f53bebf7c16b617482a4b8ae151286044c2a8237302612c7d88c8b2ad074d17c3a227d487c85b88487435c9828b8963fd132831a1f74db480a35711e151286044c2a8237302612c7d88c8b2ad074d17c3a227d487c85b88487435c97c3f9992b1a3d08f43fc92f416820f950d0d3f3cb085730e3335b7170a03ed9186622d5215afd9192d1b553cba233ff2244ded87c4d06dd82895f2b20110bbadfca1309cccb8078e2a9100cbbeaff61e4be535b1314ecb6fb99b3985c06ae00616288270b1670f7bf609b8c9c3d62e29ec49822b5417f4dad5d6048804c07f127c3f9992b1a3d08f43fc92f416820f953d255754f0e4004ac69e2e9b2e35ebc79ef39beaabf2ba23780e727eeb4e277a2757324dfeeb647dd2ab010b91af0bd3ad074d17c3a227d487c85b88487435c98bb0552673171d078cc2e6b191b4cbaa2d8c5c0bb95e29cee0cb0ea0db961a339ef39beaabf2ba23780e727eeb4e277a3cad3497d53b3c22fdd26fbb83f5cae8fe5f529bf234dcef4e76913394ae8f85244ded87c4d06dd82895f2b20110bbade57dded1cc4a151b2da4b3fa1041bc7f569f11fcae23f0661a6722466e5697ce069590e37f53bebf7c16b617482a4b8ae151286044c2a8237302612c7d88c8b29a4ef6d9c9cf8127de64c59ecc865fd89a4ef6d9c9cf8127de64c59ecc865fd8d5a6b3cf8313ced4ca89414d00adb0c2a854ed5338d047e0b65b956bd2a19fcc0d0d3f3cb085730e3335b7170a03ed91e891d349f90afb2d3f9608a7cdba0714e891d349f90afb2d3f9608a7cdba071486622d5215afd9192d1b553cba233ff216288270b1670f7bf609b8c9c3d62e299ef39beaabf2ba23780e727eeb4e277a4be535b1314ecb6fb99b3985c06ae00616288270b1670f7bf609b8c9c3d62e299a4ef6d9c9cf8127de64c59ecc865fd8ce0eef96ce210effc6a2733a73b371b1d764b219e31def9c556a602e6b236b48ba463a67b09eb3433fb94ce2d2c5ac25069590e37f53bebf7c16b617482a4b8ac9dcd54eb33f50a80149e8457d843b84ba463a67b09eb3433fb94ce2d2c5ac25e6ff67049d59429fa81ea1d14e1a4abde5beb88aa4073a5c948816378f2cc96b87b18c9563646c0652a9efd72f29cdd33cad3497d53b3c22fdd26fbb83f5cae82d8c5c0bb95e29cee0cb0ea0db961a33ce0eef96ce210effc6a2733a73b371b10ea54646c339600f167b5dd2029ba72fe5beb88aa4073a5c948816378f2cc96b5762452778b31d42ead4f81062775b69e891d349f90afb2d3f9608a7cdba07147c3f9992b1a3d08f43fc92f416820f953d255754f0e4004ac69e2e9b2e35ebc7ec49822b5417f4dad5d6048804c07f127c3f9992b1a3d08f43fc92f416820f95c8dab6841e142338fcc2d01ad0a3bce686622d5215afd9192d1b553cba233ff216288270b1670f7bf609b8c9c3d62e29ec49822b5417f4dad5d6048804c07f127c3f9992b1a3d08f43fc92f416820f950d0d3f3cb085730e3335b7170a03ed91fca1309cccb8078e2a9100cbbeaff61e0f1f25bef4b7f6442b420b861ad834aac8dab6841e142338fcc2d01ad0a3bce67c3f9992b1a3d08f43fc92f416820f953469118ed906f6b3abeff55bcdc7e5a03469118ed906f6b3abeff55bcdc7e5a00d0d3f3cb085730e3335b7170a03ed91e891d349f90afb2d3f9608a7cdba071486622d5215afd9192d1b553cba233ff2244ded87c4d06dd82895f2b20110bbad828b8963fd132831a1f74db480a35711e151286044c2a8237302612c7d88c8b29a4ef6d9c9cf8127de64c59ecc865fd8d5a6b3cf8313ced4ca89414d00adb0c22d8c5c0bb95e29cee0cb0ea0db961a33ad074d17c3a227d487c85b88487435c9828b8963fd132831a1f74db480a35711c9dcd54eb33f50a80149e8457d843b845bd9ba2fb7cea981a019c784939dfd0587b18c9563646c0652a9efd72f29cdd328d63f46073aec9a139375fd6d2917d3e5beb88aa4073a5c948816378f2cc96b87b18c9563646c0652a9efd72f29cdd30f1f25bef4b7f6442b420b861ad834aa41c1b4f70e10af5fa9e82a2b773ea7070ea54646c339600f167b5dd2029ba72fe5beb88aa4073a5c948816378f2cc96b5762452778b31d42ead4f81062775b697c3f9992b1a3d08f43fc92f416820f953469118ed906f6b3abeff55bcdc7e5a05bd9ba2fb7cea981a019c784939dfd055762452778b31d42ead4f81062775b69e891d349f90afb2d3f9608a7cdba0714fca1309cccb8078e2a9100cbbeaff61e2757324dfeeb647dd2ab010b91af0bd3ad074d17c3a227d487c85b88487435c9828b8963fd132831a1f74db480a35711e151286044c2a8237302612c7d88c8b29a4ef6d9c9cf8127de64c59ecc865fd8d5a6b3cf8313ced4ca89414d00adb0c2fc59c44e8f481760ef82750176f42291fb7648043fce2338843c67eae566b35c8bb0552673171d078cc2e6b191b4cbaa2d8c5c0bb95e29cee0cb0ea0db961a33ec49822b5417f4dad5d6048804c07f12828b8963fd132831a1f74db480a3571116d696017b13e85d5aaf28d6ac7c3d315762452778b31d42ead4f81062775b698bb0552673171d078cc2e6b191b4cbaa2d8c5c0bb95e29cee0cb0ea0db961a339a4ef6d9c9cf8127de64c59ecc865fd8ce0eef96ce210effc6a2733a73b371b1d764b219e31def9c556a602e6b236b48ba463a67b09eb3433fb94ce2d2c5ac25ce0eef96ce210effc6a2733a73b371b1d764b219e31def9c556a602e6b236b48c8dab6841e142338fcc2d01ad0a3bce67c3f9992b1a3d08f43fc92f416820f95ba463a67b09eb3433fb94ce2d2c5ac25ce0eef96ce210effc6a2733a73b371b1a25c129f9071f52f674b28cff9f4ade7244ded87c4d06dd82895f2b20110bbade891d349f90afb2d3f9608a7cdba0714828b8963fd132831a1f74db480a35711c9dcd54eb33f50a80149e8457d843b843d255754f0e4004ac69e2e9b2e35ebc7e6ff67049d59429fa81ea1d14e1a4abd569f11fcae23f0661a6722466e5697ce9ef39beaabf2ba23780e727eeb4e277abea40e40b98659cafe52c74461e7015a87b18c9563646c0652a9efd72f29cdd33cad3497d53b3c22fdd26fbb83f5cae8fe5f529bf234dcef4e76913394ae8f8516288270b1670f7bf609b8c9c3d62e29ec49822b5417f4dad5d6048804c07f127c3f9992b1a3d08f43fc92f416820f95ba463a67b09eb3433fb94ce2d2c5ac25e6ff67049d59429fa81ea1d14e1a4abd31e2e92c15e8b3afb3b4a4344f6d37a33d255754f0e4004ac69e2e9b2e35ebc7e6ff67049d59429fa81ea1d14e1a4abd31e2e92c15e8b3afb3b4a4344f6d37a341c1b4f70e10af5fa9e82a2b773ea707a25c129f9071f52f674b28cff9f4ade7244ded87c4d06dd82895f2b20110bbad011d2d66c36261ef7fb7ca949a22ed84"
ct = bytes.fromhex(hexct)
hexkey = "0123456789ABCDEF0123456789ABCDEF"
key = bytes.fromhex(hexkey)

aes = AES.new(key, AES.MODE_ECB)
pt = unpad(aes.decrypt(ct).decode('ascii'))

#Remove \n
pt = pt.strip('\n')

#Hex decode
pt = bytes.fromhex(pt).decode('ascii')

#Remove \n
pt = pt.strip('\n')

pt = pt.replace(' ', '').replace('SPACE', ' ').replace('DASH', '-').replace('DOT', '.')


morsetab = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-',
}

morsetab = {y:x for x,y in morsetab.items()}

output = ""
error = []
for letter in pt.split(' '):
	output += morsetab[letter]

output = output.replace('underscore','_').replace('bracket', '{')

output = output.upper()

#fix bracket
output = list(output)
output[-1] = '}'
output = ''.join(output)
print(output)