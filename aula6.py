# O que é um conjunto / adicionar e retirar
conjunto = {1, 2, 3, 4}
conjunto.add(5)
conjunto.discard(2)
print('Conjunto: {}'.format(conjunto))

# Método de união
conj = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8}
conjuniao = conj.union(conj2)
print('União: {}'.format(conjuniao))

# Método de intersecção
conj = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8}
conjintersec = conj.intersection(conj2)
print('Intersecção: {}'.format(conjintersec))

# Método de diferença
conj = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8}
conjdiferenca1 = conj.difference(conj2)
conjdiferenca2 = conj2.difference(conj)
print('Diferença do 1 com o 2: {}'.format(conjdiferenca1))
print('Diferença do 2 com o 1   : {}'.format(conjdiferenca2))

# Método de diferença simétrica
conj = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8}
conj_dif_sim = conj.symmetric_difference(conj2)
print('Diferença simétrica: {}'.format(conj_dif_sim))

# Pertinência
conja = {1, 2, 3}
conjb = {1, 2, 3, 4, 5}

conj_subset1 = conja.issubset(conjb)
print('O conjunto A é subconjunto do conjunto B?: {}'.format(conj_subset1))
conj_subset2 = conjb.issubset(conja)
print('O conjunto B é subconjunto do conjunto A?: {}'.format(conj_subset2))

conj_superset = conjb.issuperset(conja)
print('O conjunto B é um superconjunto do conjunto A?: {}'.format(conj_superset))

# Remoção de duplicidade de listas utilizando conjuntos
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print('Lista: {}'.format(lista))
conj_animais = set(lista)
print('Conjunto animais: {}'.format(conj_animais))
lista_animais = list(conj_animais)
print('Lista animais: {}'.format(lista_animais))