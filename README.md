# Shellcode Tester
## shellcode_poc.py
The `shellcode_poc.py` script will take arguments to build a binary to test shellcode. This script will either take an asm file or a raw PIC blob and compile it into a program to test your shellcode.

This script will use `nasm` to assemble your shellcode asm file or read your PIC blob it and write it to a proof of concept C source file and then compile that file for your given architecture. It will output your shellcode to the file 'shellcode' to execute.

Dependencies:
* nasm
* gcc 

```
usage: shellcode_poc.py [-h] (-i INPUT | -p PIC) (-x86 | -x64)

Build a linux binary to execute shellcode

optional arguments:
  -h, --help  show this help message and exit
  -i INPUT    Input file containing assembly instructions (.asm file)
  -p PIC      Shellcode PIC blob containing code to be added to testing
              executable
  -x86        Compile shellcode for x86 architecture
  -x64        Compile shellcode for x64 architecture
```

## write_binhex.py
This script takes a string of hex characters and writes it out to a binary blob (PIC blob). This can be used to test shellcode that you find online as hex characters.
To view the assembly output from your shellcode, you can run `ndisasm shellcode.bin`

This script does not take any command line arguments and must be modified to store your shellcode in the scode variable.

## Note
The following files are just for sample output and are not actually used with running the script:
* shellcode
* shellcode.asm
* poc.c

All of these files were included to provide a sample of shellcode to test. The sample shellcode being used will execute "/bin/sh"
