
#verificar qual o maior e o menor.
def verif(n1,n2):
    menor = n1 if n1 < n2 else n2
    maior = n1 if n1 > n2 else n2
    return menor,maior

if __name__ == '__main__':
    #preciso ler os valrores e armazenar numa lista com listas menores
    valores = []
    M,N = map(int,input().split())
    while N > 0 and M > 0:
        valores.append([M,N])
        M,N = map(int,input().split())

    #printar cada elemento do menor para o maior e no fim printar a soma
    for nums in valores:
        menor,maior = verif(nums[0],nums[1])
        soma = 0
        for i in range(menor,maior+1):
            print(i,end=' ')
            soma += i
        print('Sum={}'.format(soma))

