nota = int(input('Insira uma nota: '))
while nota > 10:
    nota = int(input('Nota inválida. \nInsira uma nota correta: '))

a = 0
while a < 10:
    print(a)
    a += 1

# ====================================================== #

a = int(input('Insira um valor: '))

for num in range (a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        #print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)

# ====================================================== #

a = int(input('Insira um número: '))

div = 0

for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div += 1

if div == 2:
    print('O número {} é primo.'.format(a))
else:
    print('O número {} não é primo.'.format(a))