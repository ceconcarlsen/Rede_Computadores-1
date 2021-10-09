import socket
import time
from _thread import *

host = '127.0.0.1'      # Host local
port = 8000             # Porta 8000

server = socket.socket()    # Socket() retorna um objeto socket que implementa métodos para a conexão
contThread = 0              # Contador de threads, ou seja, conexões com os multiplos clientes

try:                            # Tente vincular o socket ao enderesso fornecido (host, port)
    server.bind((host, port))
except socket.error as e:       # Exceção de erro
    print(str(e))

print('-> servidor está escutando possíveis conexões ...')
server.listen(10)        # Habilitando o servidor a aceitar conexões 


# Função que conecta o cliente
def multi_threaded_client(connection):
    connection.send(str.encode('Servidor está funcionando'))
    while True:
        data = connection.recv(2048)
        response = 'Mensagem do servidor: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()     

# Função que verifica o nº limite de threads
def limite_threads(contThread):
    if (contThread > 3):
        print('\n[ERRO]: número máximo de conexões !!!\n')

        for i in range(5,0,-1):
            print('Servidor finalizando em ', i, '...')
            time.sleep(1)
        return 1

    return 0


while True:     # Aceitando novas conexões
    cliente, endereco = server.accept()     
    print('\nConectado ao: ' + endereco[0] + ':' + str(endereco[1]))
    start_new_thread(multi_threaded_client, (cliente, ))  # Começa uma nova thread
    contThread += 1                                       # Incrementa o contador
    print('Número da Thread: ' + str(contThread))

    if(limite_threads(contThread)):                       # Se o limite for atingido
        break

server.close()                                            # Encerra o servidor
