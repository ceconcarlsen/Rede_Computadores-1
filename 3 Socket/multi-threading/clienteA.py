import socket

host = '127.0.0.1'      # Host local
port = 8000             # Porta 8000

cliente = socket.socket()   # Socket() retorna um objeto socket que implementa métodos para a conexão

print('-> esperando a resposta da conexão ...')

try:
    cliente.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    Input = input('\nOlá servidor, eu sou o cliente A')
    cliente.send(str.encode(Input))
    res = cliente.recv(1024)     # recebendo a resposta do server 
    print(res.decode('utf-8'))

cliente.close()



