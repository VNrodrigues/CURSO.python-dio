a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))

soma = a + b
subtracao = a - b
divisao = a / b
multiplicacao = a * b
resto = a % b

resultado = ('Soma: {soma}. \nSubtração: {subtracao}. \nDivisão: {divisao}. \nMultiplicação: {multiplicacao}. \nResto: {resto}'
      .format(soma=soma,
              subtracao=subtracao,
              resto=resto,
              multiplicacao=multiplicacao,
              divisao=divisao))

print(resultado)


