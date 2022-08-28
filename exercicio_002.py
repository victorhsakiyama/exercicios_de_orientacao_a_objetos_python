#Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, medida_do_lado):
        self.medida_do_lado = medida_do_lado
        self.area = int(self.medida_do_lado) * int(self.medida_do_lado)

    def __repr__(self):
        return f'Quadrado({self.medida_do_lado}, {self.area})'

    def mostra_area(self):
        print('Um quadrado de lado {}, tem área de {}.'.format(self.medida_do_lado, (str(self.area))))

    def mudar_medida(self, nova_medida):
        self.medida_do_lado = nova_medida

primeira_medida = input('Digite a medida do lado de um quadrado: ')
quadrado_1 = Quadrado(primeira_medida)
quadrado_1.mostra_area()

nova_medida = input('Digite uma nova medida: ')
quadrado_2 = Quadrado(nova_medida)
quadrado_2.mostra_area()

retornar_medida_anterior = input('Gostaria de voltar à medida anterior? Responda com [1]Sim ou [2]Não: ')
if(retornar_medida_anterior == '1'):
    quadrado_1.mostra_area()
else:
    print('Fim')



