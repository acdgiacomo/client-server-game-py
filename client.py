# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 18:33:24 2021

@author: gabri
"""

import tkinter as tk
from tkinter.constants import LEFT
import socket

resultado = 0

def pegarEscolha(escolha):
    if escolha == "1":
        return "Pedra"
    
    if escolha == "2":
        return "Papel"
    
    if escolha == "3":
        return "Tesoura"
    
    return "Nenhum"

class InterfaceEscolha:    
    def __init__(self, master):        
        self.fontePadrao = ("Arial", "21", "bold")

        self.container1 = tk.Frame(master)
        self.container1["pady"] = 60
        self.container1.pack()

        self.container2 = tk.Frame(master)
        self.container2["pady"] = 60
        self.container2.pack()

        self.container3 = tk.Frame(master)
        self.container3["pady"] = 60
        self.container3.pack()

        self.container4 = tk.Frame(master)
        self.container4["pady"] = 60
        self.container4.pack()

        self.lbTitulo = tk.Label(self.container1)
        self.lbTitulo["text"] = "Escolha entre:"
        self.lbTitulo["font"] = self.fontePadrao
        self.lbTitulo.pack()
        
        self.lbLetra = tk.Label(self.container2)
        self.lbLetra["text"] = "Nome do Usuário:"
        self.lbLetra["font"] = self.fontePadrao
        self.lbLetra.pack(side=LEFT)

        self.tbLetra = tk.Entry(self.container2)
        self.tbLetra["width"] = 35
        self.tbLetra["font"] = self.fontePadrao
        self.tbLetra.pack(side=LEFT)
        
        self.btnPedra = tk.Button(self.container3)
        self.btnPedra["text"] = "Pedra"
        self.btnPedra["font"] = self.fontePadrao
        self.btnPedra["width"] = 18
        self.btnPedra["command"] = self.enviarPedra
        self.btnPedra.pack(side=LEFT)

        self.btnPapel = tk.Button(self.container3)
        self.btnPapel["text"] = "Papel"
        self.btnPapel["font"] = self.fontePadrao
        self.btnPapel["width"] = 18
        self.btnPapel["command"] = self.enviarPapel
        self.btnPapel.pack(side=LEFT)
        
        self.btnTesoura = tk.Button(self.container3)
        self.btnTesoura["text"] = "Tesoura"
        self.btnTesoura["font"] = self.fontePadrao
        self.btnTesoura["width"] = 18
        self.btnTesoura["command"] = self.enviarTesoura
        self.btnTesoura.pack(side=LEFT)

        self.lbResultado = tk.Label(self.container4)
        self.lbResultado["text"] = ""
        self.lbResultado["font"] = self.fontePadrao
        self.lbResultado.pack()

    def enviarPedra(self):   
        self.enviarServidor(1)
        
    def enviarTesoura(self):
        self.enviarServidor(3)
        
    def enviarPapel(self):        
        self.enviarServidor(2)
        
    def enviarServidor(self, valor):
        global resultado
        resultado = valor
        letra = self.tbLetra.get()
        
        HOST = '10.0.0.216'    #endereco IP do servidor OBRIGATORIO
        PORT = 12345
        
        self.lbResultado["text"] = "Enviando Resultado para o servidor"
        
        socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        enderecoServidor = (HOST, PORT)
        socketCliente.connect(enderecoServidor)
        nome = letra.encode()
        mensagem = nome
        socketCliente.send(nome) #1 e
        
        while mensagem != 'Finalizar' :
            mensagemRecebida = socketCliente.recv(100) #2 r
            print(mensagemRecebida.decode())
            mensagemRecebida = socketCliente.recv(100) #3 r
            print(mensagemRecebida.decode())

            mensagem = str(resultado).encode()
            socketCliente.send(mensagem) #4 e
            mensagemRecebida = str(socketCliente.recv(100)) #4 r+
            mensagemRecebida = mensagemRecebida.replace("b'", "")
            
            lbResultado = mensagemRecebida[0]
            lbPontuacaoCliente = mensagemRecebida[2]
            lbPontuacaoServidor = mensagemRecebida[4]
            lbJogadaCliente = pegarEscolha(mensagemRecebida[6])
            lbJogadaServidor = pegarEscolha(mensagemRecebida[8])
            
            if lbResultado == "0":
                lbResultado = "Empate"
                
            if lbResultado == "1":
                lbResultado = "Voce Ganhou"
            
            if lbResultado == "2":
                lbResultado = "Voce Perdeu"
                
            lbMensagemFinal = "Resultado: " + lbResultado + " ( " + lbPontuacaoCliente + " - " + lbPontuacaoServidor + " )\n"
            lbMensagemFinal += "Voce Escolheu: " + lbJogadaCliente + " | Servidor Escolheu: " + lbJogadaServidor
            
            self.lbResultado["text"] = lbMensagemFinal
            mensagem = 'Finalizar'
            

        socketCliente.close()

        
    def resultado(self, valor):
        global resultado
        tipo = "Nenhum"
        
        if valor == 1:
            tipo = "Pedra"
        
        if valor == 2:
            tipo = "Papel"
        
        if valor == 3:
            tipo = "Tesoura"

        self.lbResultado["text"] = "Resultado: " + tipo
        
janelaPergunta1 = tk.Tk()
InterfaceEscolha(janelaPergunta1)
janelaPergunta1.mainloop()
