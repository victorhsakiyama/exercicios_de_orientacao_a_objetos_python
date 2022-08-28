#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __repr__(self):
        return f'Bola({self.cor}, {self.circunferencia}, {self.material})'

    def mostra_cor(self):
        print('A cor escolhida por você foi: ' + self.cor)

    def troca_cor(self, nova_cor):
        self.cor = nova_cor
        self.mostra_cor()

bola_de_basquete = Bola('laranja', '72', 'borracha')

bola_de_basquete.mostra_cor()
nova_cor = input('Digite uma cor: ')
bola_de_basquete.troca_cor(nova_cor)
