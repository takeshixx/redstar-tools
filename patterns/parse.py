#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import struct

f = open(sys.argv[1])

timestamp, = struct.unpack('<I', f.read(4))

unknown1 = f.read(1000)

package_id, = struct.unpack('<I', f.read(4))
unknown2, = struct.unpack('<I', f.read(4))
pattern_date, = struct.unpack('<I', f.read(4))
file_count, = struct.unpack('<I', f.read(4))
head_pos, = struct.unpack('<I', f.read(4))
real_size, = struct.unpack('<I', f.read(4))

pattern_count, = struct.unpack('<Q', f.read(8))

print('timestamp: {}'.format(timestamp))
print('pattern count: {}'.format(pattern_count))

patterns = []

for i in range(pattern_count):
    pattern = dict()
    pattern['reclen'], = struct.unpack('<I', f.read(4))

    if int(pattern['reclen']) is not 200:
        print(pattern['reclen'])
        break

    pattern['package_id'], = struct.unpack('<I', f.read(4))
    pattern['content'], = struct.unpack('<200s', f.read(200))
    patterns.append(pattern)

pattern_checksum, = struct.unpack('<20s', f.read(20))
print('pattern checksum: {}'.format(pattern_checksum.encode('hex')))

#print(patterns)
