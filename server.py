import socket
import random
HOST = '' #endereço servidor
PORT = 12345

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

enderecoServidor = (HOST,PORT) #ip, porta
socketServidor.bind(enderecoServidor)
socketServidor.listen(10)

while True :
    socketCliente, enderecoCliente = socketServidor.accept()
    socketServidor.close()
    print('Cliente conectado => ', enderecoCliente)
    nome = str(socketCliente.recv(100)) #1 r
    nome = nome.replace("b'", "").replace("'", "")
    mensagemEnviada = 'Conectado com sucesso! Bem vindo ao jogo ' + str(nome) + '!'
    print (mensagemEnviada) 
    socketCliente.send(mensagemEnviada.encode()) #2 e

    menuJogo = "PEDRA, PAPEL E TESOURA\n"
    menuJogo += "Bem vindo! Para jogar selecione uma opcao:\n"
    menuJogo += "1 - Pedra\n"
    menuJogo += "2 - Papel\n"
    menuJogo += "3 - Tesoura\n"

    socketCliente.send(menuJogo.encode()) #3 e

    pontuacaoCliente = 0
    pontuacaoServidor = 0

    while True :
        jogadaCliente = int(socketCliente.recv(100)) #4 r
        print(jogadaCliente)

        jogadaServidor = random.randrange(1,3)

        escolhaCliente = ""
        escolhaServidor = ""
        resultado = 0 #0 - empate | 1 - cliente | 2 - servidor
        resultaTexto = ""

        if jogadaCliente == 1 :
            escolhaCliente = 'Pedra'

            if jogadaServidor == 1 : #Empate
                escolhaServidor = 'Pedra'
                pontuacaoCliente = 0
                pontuacaoServidor = 0
                resultado = 0

            elif jogadaServidor == 2 : #Jogador perdeu
                escolhaServidor = 'Papel'
                pontuacaoCliente = 0
                pontuacaoServidor = 1
                resultado = 2

            else :
                jogadaServidor = 'Tesoura' #Jogador ganhou
                pontuacaoCliente = 1
                pontuacaoServidor = 0
                resultado = 1

        elif jogadaCliente == 2 :
            escolhaCliente = 'Papel'

            if jogadaServidor == 1 : #Jogador ganhou
                escolhaServidor = 'Pedra'
                pontuacaoCliente = 1
                pontuacaoServidor = 0
                resultado = 1

            elif jogadaServidor == 2 : #Empate
                escolhaServidor = 'Papel'
                pontuacaoCliente = 0
                pontuacaoServidor = 0
                resultado = 0

            else :
                jogadaServidor = 'Tesoura' #Jogador perdeu
                pontuacaoCliente = 0
                pontuacaoServidor = 1
                resultado = 2

        else :
            escolhaCliente = 'Tesoura'

            if jogadaServidor == 1 : #Jogador perdeu
                escolhaServidor = 'Pedra'
                pontuacaoCliente = 0
                pontuacaoServidor = 1
                resultado = 2

            elif jogadaServidor == 2 : #Jogador ganhou
                escolhaServidor = 'Papel'
                pontuacaoCliente = 1
                pontuacaoServidor = 0
                resultado = 1

            else :
                jogadaServidor = 'Tesoura' #Empate
                pontuacaoCliente = 0
                pontuacaoServidor = 0
                resultado = 0

        mensagemPrint = 'As escolhas foram: \nServidor = ' + escolhaServidor + ' | Cliente = ' + escolhaCliente + '\nResultado: '

        if resultado == 1 :
            resultaTexto = "Cliente"
        elif resultado == 2 :
            resultaTexto = "Servidor"

        if resultado == 0 :
            mensagemPrint += 'Tivemos um empate!\n'
        else :
            mensagemPrint += 'O ganhador foi: ' + resultaTexto + '.\n'

        mensagemPrint += 'Pontuacao cliente: ' + str(pontuacaoCliente) + ' | Pontuacao servidor: ' + str(pontuacaoServidor) + '\n'

        print(mensagemPrint)

        with open('ganhador.txt','w') as arq:
            arq.write(mensagemPrint+'\n')

        mensagemEnviada = str(resultado) + '|' + str(pontuacaoCliente) + '|' + str(pontuacaoServidor) + '|' + str(jogadaCliente) + '|' + str(jogadaServidor)

        socketCliente.send(mensagemEnviada.encode()) #4 e

print('Conexao finalizada com o cliente  ' , enderecoCliente)
socketCliente.close()