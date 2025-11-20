import numpy as np
import numpy.fft

def chiffre():
    FLAG = open("flag.txt", "rb").read()

    array = np.array([], dtype=np.complex64)
    for c in FLAG:
        array = np.append(array, c)


    # Compute inverse FFT
    result = np.array(np.fft.ifft(array, n=64), dtype=np.complex64)

    result.tofile("challenge")


def dechiffre():
    result = np.fromfile("/home/werenn/Downloads/fftea", dtype=np.complex64)
    array = np.fft.fft(result, n=64)
    flag_bytes = bytes([int(round(c.real)) for c in array])    
    flag = flag_bytes.split(b'\x00')[0]
    
    return flag

print(dechiffre())