import socket

morse_dict = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9'
}

def morse_to_alpha(message: str) -> str:
    list_char = message.split(" ")
    new_message = ""
    for char in list_char:
        new_message += morse_dict[char]
    return new_message


def alpha_to_morse(message: str) -> str:
    alpha_to_morse_dict = {v: k for k, v in morse_dict.items()}
    new_message = ""
    for char in message:
        new_message += alpha_to_morse_dict[char] + " "
    return new_message


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 4000))

try:
    while True:
        data = client.recv(1024).decode()
        print(f"Reçu: {data}")

        message = alpha_to_morse("FLAG").strip() + '\n'
        print(f"Envoie: {message}")
        client.send(message.encode())



        

finally:
    client.close()