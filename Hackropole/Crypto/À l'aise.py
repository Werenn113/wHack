text = "Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf."

def decrypt_vigenere(text: str, key: str) -> str:
    new_text = ""
    text = text.lower()
    key = key.lower()
    i = 0

    for char in text:
        if char.islower():
            new_text += chr((ord(char) - ord(key[i%len(key)]) + 26) % 26 + ord('a'))
            i += 1
        else:
            new_text += char

    return new_text


print(decrypt_vigenere(text, "FCSC"))