


if __name__ == '__main__':
    N = input() #não vou usar para nada, porém o problema pede a leitura
    lista = list(map(int,input().split()))
    menor = min(lista)
    index = lista.index(menor)
    print(f'Menor valor: {menor}\n' + f'Posicao: {index}')