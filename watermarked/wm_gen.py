#!/usr/bin/env python
# Generates a watermark unique to the system when run on Red Star OS.
# Tested to be compatible with Red Star's default Python 2.6, and does not require pycrypto.

import os, sys, time
from shutil import copyfile

# Assume this file exists as the basis for watermarking
fname = "preview_bottle_original.jpg"

# Setup constants and parameters
eof_size = 6
checksum_size = 1
wm_size = 24
eof = "000000454f46".decode("hex")
file_size = os.path.getsize(fname)

with open(fname, "r+") as f:
   # Read the end of the file looking for the watermark EOF signature
   f.seek(file_size - eof_size)
   feof = f.read(eof_size)
   if feof == eof:
      f.seek(file_size - eof_size - checksum_size)

      # The checksum value is just a count of the number of watermark bytes to read back in the file
      checksum = ord(f.read(checksum_size))
      num_wm = checksum / wm_size
      print "Found %d watermarks, removing" % (num_wm)
      f.seek(file_size - eof_size - checksum_size - (wm_size * num_wm))
      f.truncate()

copyfile(fname, "tmp_" + fname)

# Open and close new file to trigger watermarking
print "Triggering watermark"
with open("tmp_" + fname, 'rb') as tmpf:
   time.sleep(1)

file_size = os.path.getsize("tmp_" + fname)
with open("tmp_" + fname, "rb") as f:
   # Read the end of the file looking for the watermark EOF signature
   f.seek(file_size - eof_size)
   feof = f.read(eof_size)
   if feof != eof:
      os.remove("tmp_" + fname)
      sys.exit("Watermark EOF magic not found. This system is not running Red Star OS and is an imperialist aggressor.")
   f.seek(file_size - eof_size - checksum_size)

   # The checksum value is just a count of the number of watermark bytes to read back in the file
   checksum = ord(f.read(checksum_size))
   num_wm = checksum / wm_size
   print "Found %d watermarks (1 expected)" % (num_wm)

   # Iterate through all watermarks, and print both the ciphertext and plaintext
   for i in range(1, num_wm + 1):
      f.seek(file_size - eof_size - checksum_size - (wm_size * i))
      wm = f.read(wm_size)
      print "\nCiphertext: " + ":".join("{0:02x}".format(ord(c)) for c in wm)
os.remove("tmp_" + fname)
