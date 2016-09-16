# Tools and samples of Red Star OS watermarking

Several samples of how Red Star's watermarking alters files are provided.

## Watermark format

The general format of the watermarks is:

[24 byte watermark 1]..[24 byte watermark n][4 byte checksum][3 byte EOF mark]

The checksum is 4 byte little-endian integer containing a count of the total number of bytes of the preceeding watermarks, i.e. 24 for 1 watermark, 48 for 2, etc.

## Watermark encryption

The 24 byte mark itself is ciphertext. The plaintext can be decrypted using a DES ECD mode cipher, with the fixed and unsalted key "0706050403020100". The plaintext always begins with "WM", and is padded with null bytes to reach the 24 byte length required to satisfy the DES block cipher's requirement that the plaintext length be a multiple of 8 bytes. For example:

	Ciphertext: 79:08:df:d0:e0:92:b2:d1:28:24:7e:20:31:59:75:b2:5a:13:a0:e6:29:4b:75:b1
	Plaintext: WM8295FF513293A
