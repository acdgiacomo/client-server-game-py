import socket
HOST = ''           #endereco de IP é o da máquina atual
PORT = 12345
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST,PORT)
socketServidor.bind(enderecoServidor)
socketServidor.listen(1)
while True :
    socketCliente, enderecoCliente = socketServidor.accept()
		socketServidor.close()
        print('Cliente conectado => ', enderecoCliente)
        nome = socketCliente.recv(100)
        mensagemEnviada = 'Conectado com sucesso'
        socketCliente.send(mensagemEnviada.encode())
        while True :
            mensagem = socketCliente.recv(100)
            if not mensagem : break
            print(nome, " : ", mensagem.decode())
            if mensagem.decode() == 'Oi' :
                socketCliente.send(mensagem)
            else :
                mensagemEnviada = 'Não sei do que você esta falando'
                socketCliente.send(mensagemEnviada.encode())
        print('Conexao finalizada com o cliente  ' , enderecoCliente)
        socketCliente.close();
        sys.exit(0)