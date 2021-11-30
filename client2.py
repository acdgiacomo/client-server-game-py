import socket
HOST = '10.0.0.216'    #endereco IP do servidor OBRIGATORIO
PORT = 12345

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketCliente.connect(enderecoServidor)
print ('* Pedra, papel, tesoura *')
nome = input('Digite seu nome : ').encode()
mensagem = nome
socketCliente.send(nome) #1 e
while mensagem != 'Finalizar' :
    mensagemRecebida = socketCliente.recv(100) #2 r
    print(mensagemRecebida.decode())
    mensagemRecebida = socketCliente.recv(100) #3 r
    print(mensagemRecebida.decode())

    mensagem = input('-> ').encode()
    socketCliente.send(mensagem) #4 e
    mensagemRecebida = socketCliente.recv(100) #4 r
    print(mensagemRecebida.decode())
    mensagem = 'Finalizar'

socketCliente.close()