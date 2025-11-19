import socket

HOST = '127.0.0.1'
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

try:
    while True:
        # Recevoir les données
        data = client.recv(1024).decode()
        
        # Vérifier si la connexion est fermée
        if not data:
            print("Connexion fermée par le serveur")
            break
        
        print(f"Reçu: {data}")

        lines = data.split('\n')

        for line in lines:
            if line.startswith('>>> '):
                line = line.lstrip('>>> ').rstrip()
                
                # Inverser les bytes (pas la string)
                reversed_data = line[::-1] + '\n'
                print(f"Envoi: {reversed_data}")
                
                # Envoyer la réponse
                client.send(reversed_data.encode())

finally:
    client.close()
    print("Connexion fermée")
