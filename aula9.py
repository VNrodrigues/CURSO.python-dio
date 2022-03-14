import shutil

# Como gerar e escrever um arquivo
def escrever_arq(texto):
    diretorio = 'E:/repos/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def att_arq(nome_arq, texto):
    arquivo = open(nome_arq, 'a')
    arquivo.write(texto)
    arquivo.close()

# Como ler informações de um arquivo
def ler_arq(nome_arq):
    arquivo = open(nome_arq, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arq):
    arquivo = open(nome_arq, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arq(nome_arq):
    shutil.copy(nome_arq, 'E:/repos/')

def mover_arq(nome_arq):
    shutil.move(nome_arq, 'E:/repos/')

if __name__ == '__main__':
    mover_arq('notas.txt')
    # copia_arquivo('notas.txt')
    # print(lista_media)
    # escrever_arq('Primeira linha.\n')
    # aluno = 'Cesar 7, 9, 3, 8\n'
    # att_arq('notas.txt', aluno)
    # att_arq('Terceira linha.\n')
    # ler_arq('teste.txt')

# Como trabalhar com as informações de um arquivo

# Como trabalhar melhor com as Strings

# Lambda

# Como copiar e mover arquivos