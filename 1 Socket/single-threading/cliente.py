import socket

HOST = '127.0.0.1'                                        # Localhost
PORT = 5050                                               # Porta

C = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # IPv4 e TCP 

C.connect((HOST,PORT))                    # Conectando no HOST na porta PORT

C.sendall(str.encode('Teste :)')) # Mensagem enviada para o Servidor

data = C.recv(1024)                       # Dados ecoados do Servidor

print("Mensagem ecoada:", data.decode()) 


