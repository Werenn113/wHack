"""
On sait que le prog récupère la position de la sourie, donc on cherche la fonction dans les dll windows.
Un fois qu'on l'a trouvé, on regarde où elle est utilisé. 
Dans cette fonction on voit un test sur un registre qui a été xoré (donc forcément faux).

Avec le prog python suivant on remplace le contenu de la fonction qui va faire en sorte que ça ne bouge plus.
"""


with open('/home/werenn/Downloads/CATCHME.EXE', 'r+b') as f:
    start_adress = 0x00401000
    file_offset = 0X0
    offset_function = (0x00401110 - start_adress) + file_offset

    a = f.seek(1296)
    f.write(b"\x31\xC0\xC3" + b"\x90" * 129)