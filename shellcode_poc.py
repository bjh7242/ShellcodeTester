#!/usr/bin/python
# Dependencies: nasm, gcc
# 
# shellcode.asm => file containing assembly instructions
# nasm -o shellcode.bin shellcode.asm
# xxd -ps shellcode.bin | tr -d '\n'
# ndisasm shellcode.bin
# python3 shellcode_poc.py
# gcc -o shellcode -zexecstack poc.c
# ./shellcode

import argparse
import binascii
import subprocess
import sys

def build_shellcode():
	if args.input:
		try:
			nasm_args = ['nasm','-o','shellcode.bin','-f','bin', args.input]
			print("Running: %s" % ' '.join(nasm_args))
			subprocess.call(nasm_args)
			with open('shellcode.bin', 'rb') as f:
				shellcode = f.read()
		except Exception as e:
			print(e)
			sys.exit()

	elif args.pic:
		with open(args.pic, 'rb') as f:
			shellcode = f.read()
	
	hexshellcode = binascii.hexlify(shellcode)
	scode = r"\x" + r"\x".join(hexshellcode.decode()[n : n+2] for n in range(0, len(hexshellcode.decode()), 2))
	print("Shellcode Hex Codes:")
	print(scode)
	
	poc = """
	char scode[] = "%s";
	
	int main(int argc, char **argv) {
		int (*one)();
		one = (int(*)())scode;
		(int)(*one)();
	}
	""" % scode
	
	with open('poc.c', 'w') as w:
		w.write(poc)
	
	if args.x86:
		gcc_args = ['gcc','-o','shellcode','-m32','-O0','-zexecstack','poc.c']
	elif args.x64:
		gcc_args = ['gcc','-o','shellcode','-m64','-O0','-zexecstack','poc.c']
	else:
		print("Error: unknown architecture")
	
	print("\nCompiler Options:")
	print(' '.join(gcc_args))
	
	subprocess.Popen(gcc_args)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Build a linux binary to execute shellcode')
	inputfile = parser.add_mutually_exclusive_group(required=True)
	inputfile.add_argument('-i', dest='input', help="Input file containing assembly instructions (.asm file)")
	inputfile.add_argument('-p', dest='pic', help="Shellcode PIC blob containing code to be added to testing executable")
	arch = parser.add_mutually_exclusive_group(required=True)
	arch.add_argument('-x86', dest='x86', action="store_true", help="Compile shellcode for x86 architecture")
	arch.add_argument('-x64', dest='x64', action="store_true", help="Compile shellcode for x64 architecture")
	args = parser.parse_args()
	print(args.pic)
	print(args.input)

	build_shellcode()
