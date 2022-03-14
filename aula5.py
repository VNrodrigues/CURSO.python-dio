# Como criar uma lista
lista = [1, 2, 5, 7]
lista_animais = ['gato', 'cachorro', 'elefante']

# Manipular listas
print(lista_animais[1])
soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

lista_animais[0] = 'macaco'
print(lista_animais)

lista.sort
print(lista)

lista_animais.sort()
print(lista_animais)

lista_animais.reverse()
print(lista_animais)

animal = str(input('Nome do animal: '))
if animal in lista_animais:
    print('{} está na lista.'.format(animal))
else:
    print('{} não está na lista. Será incluido.'.format(animal))
    lista_animais.append('{}'.format(animal))
    print('Esta é a nova lista: {}'.format(lista_animais))

# soma da lista
soma = sum(lista)
print('A soma da lista é: {}'. format(soma))

# valor máx da lista
maximo = max(lista)
print('O valor máximo é: {}'. format(maximo))

tupla = (1, 10, 12, 14)
print(tupla[2])
print(len(tupla))

# Conversão de lista e tuplas
tupla_animal = tuple(lista_animais)
print(tupla_animal)

lista_animais2 = list(tupla_animal)
print(lista_animais2)