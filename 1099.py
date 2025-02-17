
def verif(n1,n2):
    menor = n1 if n1 < n2 else n2
    maior = n1 if n1 > n2 else n2
    return menor,maior

if __name__ == '__main__':
    valores = []
    N = int(input())
    for i in range(N):
        X,Y = map(int,input().split())
        valores.append([X,Y])

    for nums in valores:
        menor,maior = verif(nums[0],nums[1])
        soma = 0
        for i in range(menor+1,maior):
            if i % 2 == 1:
                soma += i
        print('{}'.format(soma))