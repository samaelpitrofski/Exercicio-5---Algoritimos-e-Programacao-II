'''
Aula 07
▷Construa um algoritmo para implementar a classe Retângulo que possui os atributos: altura e largura.
▷A classe deve ter os seguintes métodos:
-Método construtor
-Método que calcula a área do retângulo ( altura * largura) e retorna o resultado
-Método que imprime os valores dos atributos da classe.

'''

class Retangulo :

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def cacular_area(self):
        area = self.altura * self.largura
        print("A area do retangulo é de {}. " .format(area))
        return area

    def printvalores(self):
        print("O retangulo possui {} de altura e {} de largura." .format(self.altura, self.largura))


retangulo = Retangulo(5,2)

Retangulo.printvalores(retangulo)
Retangulo.cacular_area(retangulo)
