import socket

cliente = socket.socket()
host = '127.0.0.1'
port = 8000

print('-> esperando a resposta da conexão ...')

try:
    cliente.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    Input = input('\nOlá servidor, eu sou o cliente C')
    cliente.send(str.encode(Input))
    res = cliente.recv(1024)     # recebendo a resposta do server 
    print(res.decode('utf-8'))

cliente.close()