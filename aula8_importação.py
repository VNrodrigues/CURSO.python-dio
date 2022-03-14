from aula7_televisão import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Contador de letras do total da lista: {}'.format(total_letras))