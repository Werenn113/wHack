from Crypto.Util.strxor import strxor

def chiffrage():
    import os
    from Crypto.Util.number import long_to_bytes
    from Crypto.Util.strxor import strxor

    FLAG = open("flag.txt", "rb").read()

    key = os.urandom(4) * 20
    c = strxor(FLAG, key[:len(FLAG)])
    print(c.hex())

result = "d91b7023e46b4602f93a1202a7601304a7681103fd611502fa684102ad6d1506ab6a1059fc6a1459a8691051af3b4706fb691b54ad681b53f93a4651a93a1001ad3c4006a825"


def dechiffre(enc):
    enc = bytes.fromhex(enc)
    # key = b'FCSC'
    # msg = strxor(enc[:4], key)

    key = b'\x9fX#`' * 20
    msg = strxor(enc, key[:len(enc)])

    print(msg)


dechiffre(result)