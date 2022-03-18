class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input(('Entre com uma nota de 0 a 10: ')))
        print(x)
        if x > 10:
            raise InputError('A nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('A nota não pode ser menor que 10')
        break
    except ValueError:
        print('Valor inválido, deve-se digitar apenas número')
    except InputError as ex:
        print(ex)
