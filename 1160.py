T = int(input())
testes = []
for _ in range(T):
    testes.append(input().split())

for i in range(T):
    PA,PB,G1,G2 = int(testes[i][0]),int(testes[i][1]),float(testes[i][2]),float(testes[i][3])
    soma = 0
    message = ''
    while PA <= PB:
        soma +=1
        PA += int(((G1/100) * PA))
        PB += int(((G2/100) * PB))
        if soma > 100:
            message = 'Mais de 1 seculo.'
            break
        else:
            message = f'{soma} anos.'
    print(message)



