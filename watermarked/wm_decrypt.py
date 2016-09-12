#!/usr/bin/env python3
# Parses and decrypts watermarks from Red Star OS 3.0.
# Currently supports only image watermarks.
import sys
import struct
try:
    from Crypto.Cipher import DES
except ImportError:
    print('Run: pip install pycrypto')
    sys.exit(1)


KEY = b'\x07\x06\x05\x04\x03\x02\x01\x00'


def wm_decrypt(wm):
    c = DES.new(KEY, DES.MODE_ECB)
    return c.decrypt(wm)


if __name__ == '__main__':
    f = open(sys.argv[1], 'rb')
    f.seek(-3, 2)
    if f.read(3) != b'EOF':
        print('File does not include a watermark')
        sys.exit(1)
    f.seek(-7, 2)
    # The total length of the watermarks is
    # a 32 Bit little endian integer right
    # before the 'EOF' sequence.
    size = struct.unpack('<I', f.read(4))[0]
    if not size:
        print('Invalid size')
        sys.exit(1)
    f.seek(0)
    wms = f.read(size)
    # Watermarks are always 24 Byte long.
    if len(wms) % 24 != 0:
        print('Invalid watermark count')
        sys.exit(1)

    for i in [wms[i:i+24] for i in range(0, len(wms), 24)]:
        print(wm_decrypt(i))

