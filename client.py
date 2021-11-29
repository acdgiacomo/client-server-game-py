import socket
HOST = '192.168.0.3'    #endereco IP do servidor OBRIGATORIO
PORT = 12345
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST, PORT)
socketCliente.connect(enderecoServidor)
print ('Digite X para sair')
nome = input('Digite seu nome : ').encode()
mensagem = nome
socketCliente.send(nome)
while mensagem != b'X' :
    mensagemRecebida = socketCliente.recv(100)
    print('Mensagem Recebida = ', mensagemRecebida.decode())
    mensagem = input('Digite sua mensagem : ').encode()
    socketCliente.send(mensagem)
socketCliente.close();