#Classe Retangulo: Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        self.area = int(self.comprimento) * int(self.largura)
        self.perimetro = (int(self.comprimento) * 2) + (int(self.largura) * 2)

    def __repr__(self):
        return f'Retangulo({self.comprimento}, {self.largura}, {self.area})'

    def mostrar_area_e_perimetro(self):
        print('Um retangulo de comprimento {} e largura {}, tem área de {}, e perimetro {}.'.format(self.comprimento, self.largura, (str(self.area)), (str(self.perimetro))))

    def mudar_medida(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

comprimento = input('Digite o comprimento do seu retangulo: ')
largura = input('Agora a largura: ')
retangulo_1 = Retangulo(comprimento, largura)
retangulo_1.mostrar_area_e_perimetro()

novo_comprimento = input('Digite um novo comprimento: ')
nova_largura = input('Agora uma nova largura: ')
retangulo_2 = Retangulo(novo_comprimento, nova_largura)
retangulo_2.mostrar_area_e_perimetro()

retornar_medida_anterior = input('Gostaria de voltar à medida anterior? Responda com [1]Sim ou [2]Não: ')
if(retornar_medida_anterior == '1'):
    retangulo_1.mostrar_area_e_perimetro()
else:
    print('Fim')
