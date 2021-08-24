import socket

HOST = '127.0.0.1'                                   # Localhost
PORT = 5050                                          # Porta
 
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Padrão 
''' 
Objeto socket da biblioteca socket; 
socket.AF_INET: representa a família do protocolo (IPv4);
socket.SOCK_STREAM: representa o tipo de protocolo de transporte (TCP);

'''                                             
S.bind((HOST,PORT))             # Faz a ligação do socket com o endereço desejado 
S.listen()                      # Habilita o servidor a aceitar conexões

print("Aguardando conexão de um cliente ...")

conn, ender = S.accept()  
'''
Aceita a conexão;
Retornando socket para enviar e receber dados (conn);
Endereço ligado ao socket (ender);
'''
print("Conectado em", ender)                         
 
while True:                                  # Aceitando novas conexões
    data = conn.recv(1024)                   # Recebe dados pelo socket (1024 bytes)
    if not data:
        print("Conexão fechada :)")
        conn.close()
        break 
    conn.sendall(data)                       # Ecoando os dados de volta para o cliente