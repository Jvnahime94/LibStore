# AV2 JOÃO VICTOR NAHIME 
# 201703207271
# LIBSTORY DE JOÃO
def bubbleSort(L, ordem, opcao):
    if ordem == 'C':
        for i in range(len(L)-1):
            for j in range(0,len(L)-i-1):
                if L[j][opcao] > L[j+1][opcao]:
                    L[j], L[j+1] = L[j+1], L[j]
    else:
        for i in range(len(L)-1):
            for j in range(0,len(L)-i-1):
                if L[j][opcao] < L[j+1][opcao]:
                    L[j], L[j+1] = L[j+1], L[j]
    return L

'''
def mostrarL(L):
----print()
----for i in range(len(L)):
--------print('{} '.format(L[i]))
'''

def mostrarL(L):
    print()
    print("LIVROS")
    print("------\n")
    for i in range(len(L)):
        print('Título ..: {}'.format(L[i][0]))
        print('Autor ...: {}'.format(L[i][1]))
        print('Páginas .: {}'.format(L[i][2]))
        print('Preço ...: R$ {:.2f}\n'.format(L[i][3]))

# Nome do livro, Nome do autor, Qtd p., Preço
L = [
      ['A','X',10,10],
      ['B','Y',20,34],
      ['C','Z',25,65],
      ['D','W',12,78],
      ['E','T',22,93],
      ['F','U',34,22],
      ['G','V',7,17],
      ['H','G',9,54],
      ['I','H',45,67],
      ['J','I',78,78]
]

while True:
    print("\n1 - Inserir livro")
    print("2 - Remover livro")
    print("3 - Visualizar livros")
    print("4 - Sair")

    opcao = int(input("\nOpção: "))

    if opcao == 1:
        titulo = input("\nTitulo do livro: ")
        autor = input("Autor do livro: ")
        paginas = int(input("Número de páginas: "))
        preco = float(input("Preço do livro: "))
        L.append([titulo.upper(),autor.upper(),paginas,preco])
    elif opcao == 2:
        titulo = input("\nTitulo do livro: ")
        for i in range (len(L)):
            if L[i][0] == titulo:
                posicao = i
                break
        del L[posicao]
    elif opcao == 3:
        print("\n1 - Ordem normal")
        print("2 - Ordem crescente")
        print("3 - Ordem decrescente")
        print("4 - Voltar")

        opcao2 = int(input("\nOpção: "))

        if (opcao > 0) and (opcao < 4):

            if opcao2 == 1:
                mostrarL(L)
            elif opcao2 == 2:
                print("\n1 - Ordem crescente por título")
                print("2 - Ordem crescente por nome do autor")
                print("3 - Ordem crescente por quantidade de página(s)")
                print("4 - Ordem crescente por preço")
                print("5 - Voltar")

                opcao2 = int(input("\nOpção: "))
                if (opcao2 > 0) and (opcao2 < 5):
                    mostrarL(bubbleSort(L,'C',(opcao2-1)))
            elif opcao == 3:
                print("\n1 - Ordem decrescente por título")
                print("2 - Ordem decrescente por nome do autor")
                print("3 - Ordem decrescente por quantidade de página(s)")
                print("4 - Ordem decrescente por preço")
                print("5 - Voltar")

                opcao2 = int(input("\nOpção: "))
                if (opcao2 > 0) and (opcao2 < 5):
                    mostrarL(bubbleSort(L,'D',(opcao2-1)))
    elif opcao == 4:
        break
