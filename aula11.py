# Como lançar uma exceção genérica
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    divisao = 10 / 0
    print('Fechando o arquivo')
    arquivo.close()
except ZeroDivisionError:
    print('Não é possível realizar esta operação.')
except IndexError:
    print('Erro ao acessar um índice  inválido da lista')
except BaseException as ex:
    print('Erro desconhecido: {}'.format(ex))
else:
    print('Executa quando não tem erro')
finally:
    print('Sempre executa')
    arquivo.close()
