a = int(input('Nota do primeiro bimestre: '))
while a > 10:
    a = int(input('Nota inválida. '
                  '\nNota do primeiro bimestre: '))

b = int(input('Nota do segundo bimestre: '))
while b > 10:
    b = int(input('Nota inválida. '
                  '\nNota do segundo bimestre: '))

c = int(input('Nota do terceiro bimestre: '))
while c > 10:
    c = int(input('Nota inválida. '
                  '\nNota do terceiro bimestre: '))

d = int(input('Nota do quarto bimestre: '))
while d > 10:
    d = int(input('Nota inválida. '
                  '\nNota do quarto bimestre: '))

media = (a + b + c + d) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
print('A média do aluno é de: {}'.format(media))
else:
    print('Foi informado alguma nota errada.')


# ====================================================================================== #

a = int(input('Calculadora de ímpar ou par \nInsira um valor: '))
b = int(input('Insira outro valor: '))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b > 0:
    print('Um dos números inseridos é par.')
else:
    print('Nenhum número par foi digitado.')

# ====================================================================================== #

a = int(input('CALCULADORA \nEntre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
c = int(input('Entre com o terceiro valor: '))

if a > b and a > c:
    print('O maior número é: {}.'.format(a))
elif a == b and a == c:
    print('Os números são iguais')
elif b > a and b > c:
    print('O maior número é: {}.'.format(b))
else:
    print('O maior número é: {}.'.format(c))
print('Fim do programa.')
