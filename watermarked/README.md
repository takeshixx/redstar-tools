# Tools and samples of Red Star OS watermarking

Several samples of how Red Star's watermarking alters files are provided.

## Watermark format

The general format of the watermarks is:

[24 byte watermark a]..[24 byte watermark n][1 byte checksum][6 byte EOF mark]

The checksum is a count of the total number of bytes of the preceeding watermarks, i.e. 24 for 1 watermark, 48 for 2, etc. 11 or more watermarks would create a checksum > 255, overflowing the checksum byte; what happens in this case has not been tested.

## Watermark encryption

The 24 byte mark itself is ciphertext. The plaintext can be decrypted using a DES ECD mode cipher, with the fixed and unsalted key "0706050403020100". The plaintext always begins with "WM", and is padded with null bytes to reach the 24 byte length required to satisfy the DES block cipher's requirement that the plaintext length be a multiple of 8 bytes. For example:

	Ciphertext: 79:08:df:d0:e0:92:b2:d1:28:24:7e:20:31:59:75:b2:5a:13:a0:e6:29:4b:75:b1
	Plaintext: WM8295FF513293A
