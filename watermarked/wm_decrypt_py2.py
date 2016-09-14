#!/usr/bin/env python
# Python 2 version of wm_decrypt.py
# Prints ciphertext watermarks for compatibity with wm_gen.py

import os, sys
from Crypto.Cipher import DES

# Expecting filename as the only argument
if len(sys.argv) != 2:
   sys.exit("Usage: " + sys.argv[0] + " <filename>")
fname = sys.argv[1]

# Setup constants and parameters
eof_size = 6
checksum_size = 1
wm_size = 24
eof = "000000454f46".decode("hex")
des_ecb_key = "0706050403020100".decode("hex")
des_mode = DES.MODE_ECB
des_iv = "00000000"
file_size = os.path.getsize(fname)

with open(fname, 'rb') as f:
   # Read the end of the file looking for the watermark EOF signature
   f.seek(file_size - eof_size)
   feof = f.read(eof_size)
   if feof != eof:
      sys.exit("Watermark EOF magic not found. File not from Best Korea.")
   f.seek(file_size - eof_size - checksum_size)

   # The checksum value is just a count of the number of watermark bytes to read back in the file
   checksum = ord(f.read(checksum_size))
   num_wm = checksum / wm_size
   print "Found %d watermarks" % (num_wm)
   des = DES.new(des_ecb_key, des_mode, des_iv)

   # Iterate through all watermarks, and print both the ciphertext and plaintext
   for i in range(1, num_wm + 1):
      f.seek(file_size - eof_size - checksum_size - (wm_size * i))
      wm = f.read(wm_size)
      print "\nCiphertext: " + ":".join("{0:02x}".format(ord(c)) for c in wm)
      print "Plaintext: " + des.decrypt(wm)
