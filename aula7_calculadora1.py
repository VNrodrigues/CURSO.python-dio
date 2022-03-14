# # Como declarar métodos e funções
# def soma(a, b):
#     return a + b
#
# def multiplicacao(a, b):
#     return a * b
#
# def subtracao(a, b):
#     return a - b
#
# def divisao(a, b):
#     return a - b
#
# print('A soma é: {}'.format(soma(1, 2)))
# print('A multiplicação é: {}'.format(multiplicacao(3, 4)))
# print('A subtração é: {}'.format(subtracao(10, 2)))
# print('A divisão é: {}'.format(divisao(12, 2)))

# Como implementar classes
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':

    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.valor_b)

    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())
