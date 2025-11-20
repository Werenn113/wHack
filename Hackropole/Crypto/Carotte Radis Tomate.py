import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def chiffrage():
    import os
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad

    key = os.urandom(32)
    print("carotte = ", int.from_bytes(key) % 17488856370348678479)
    print("radis   = ", int.from_bytes(key) % 16548497022403653709)
    print("tomate  = ", int.from_bytes(key) % 17646308379662286151)
    print("pomme   = ", int.from_bytes(key) % 14933475126425703583)
    print("banane  = ", int.from_bytes(key) % 17256641469715966189)

    flag = open("flag.txt", "rb").read()
    E = AES.new(key, AES.MODE_ECB)
    enc = E.encrypt(pad(flag, 16))
    print(f"enc = {enc.hex()}")

carotte =  392278890668246705
radis   =  4588810924820033807
tomate  =  17164682861166542664
pomme   =  12928514648456294931
banane  =  5973470563196845286
enc = "2da1dbe8c3a739d9c4a0dc29a27377fe8abc1c0feacc9475019c5954bbbf74dcedce7ed3dc3ba34fa14a9181d4d7ec0133ca96012b0a9f4aa93c42c61acbeae7640dd101a6d2db9ad4f3b8ccfe285e0d"


def dechiffre(enc, key):
    enc = bytes.fromhex(enc)
    key = key.to_bytes(32, 'big')

    cipher = AES.new(key, AES.MODE_ECB)
    dechiffred = cipher.decrypt(enc)

    return unpad(dechiffred, AES.block_size)


def ctr(remainders, modules) -> int:
    n = math.prod(modules)
    x = 0
    
    for i in range(len(modules)):
        n_i = modules[i]
        n_i_c = n // n_i

        r, u, v = euclide_etendu(n_i, n_i_c)
        
        e_i = v * n_i_c # type: ignore

        x += remainders[i] * e_i

    return x % n


def euclide_etendu(r, r2, u = 1, v = 0, u2 = 0, v2 = 1):
    while r2 != 0:
        q = r // r2
        r, u, v, r2, u2, v2 = r2, u2, v2, r - q * r2, u - q * u2, v - q * v2
    return r, u, v


remainders = [
    392278890668246705,
    4588810924820033807,
    17164682861166542664,
    12928514648456294931,
    5973470563196845286
]

modules = [
    17488856370348678479,
    16548497022403653709,
    17646308379662286151,
    14933475126425703583,
    17256641469715966189
]

key = ctr(remainders, modules)
print(dechiffre(enc, key))