from tkinter import *

class Friends:
    def __init__(self):
        self.pessoa = input('Quem você é? ')
        self.identificacao = []

    def informações (self, nome, idade, turno):
        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade: ')
        turno = input('Digite o turno que você estuda: ')