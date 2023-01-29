# Code generated by font_to_py.py.
# Font: Hack Regular Nerd Font Complete Mono Windows Compatible.ttf Char set: 
# Cmd: .\font_to_py.py C:\Users\zachs\AppData\Local\Microsoft\Windows\Fonts\Hack Regular Nerd Font Complete Mono Windows Compatible.ttf 24 hacknf24.py --charset 
version = '0.33'

def height():
    return 25

def baseline():
    return 25

def max_width():
    return 20

def hmap():
    return False

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 63

def max_ch():
    return 62018

_font =\
b'\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x1e\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00\x07\x00'\
b'\xe0\x00\x07\xf0\xf1\x01\x07\xf8\xf1\x01\x07\xfc\xf1\x01\x07\x1e'\
b'\xe0\x00\x0f\x0f\x00\x00\xfe\x07\x00\x00\xfe\x03\x00\x00\xfc\x01'\
b'\x00\x00\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x0e\x00'\
b'\x00\x00\x06\x00\x00\x00\x07\x00\xe0\x00\x07\xf0\xf1\x01\x07\xf8'\
b'\xf1\x01\x07\xfc\xf1\x01\x07\x1e\xe0\x00\x0f\x0f\x00\x00\xfe\x07'\
b'\x00\x00\xfe\x03\x00\x00\xfc\x01\x00\x00\x70\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x14\x00\x00\xff\x07\x00\x00\x01\x04\x00\x00\xfd\x05\x00\x00\xfd'\
b'\x05\x00\x00\xfd\x05\x00\x00\xfd\x05\x00\x00\xfd\x05\x00\x00\xfd'\
b'\x05\x00\x00\xfd\x05\x00\x00\xfd\x05\x00\x00\x01\x04\x00\x00\x01'\
b'\x04\x00\x00\x01\x04\x00\x00\x01\x04\x00\x00\x01\x04\x00\x00\x01'\
b'\x04\x00\x00\x01\x04\x00\x00\x01\x04\x00\x00\x87\x07\x00\x00\xfc'\
b'\x00\x00'

_sparse =\
b'\x3f\x00\x0b\x00\x42\xf2\x16\x00'

_mvfont = memoryview(_font)
_mvsp = memoryview(_sparse)
ifb = lambda l : l[0] | (l[1] << 8)

def bs(lst, val):
    while True:
        m = (len(lst) & ~ 7) >> 1
        v = ifb(lst[m:])
        if v == val:
            return ifb(lst[m + 2:])
        if not m:
            return 0
        lst = lst[m:] if v < val else lst[:m]

def get_ch(ch):
    doff = bs(_mvsp, ord(ch)) << 3
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((25 - 1)//8 + 1) * width
    return _mvfont[doff + 2:next_offs], 25, width
 
