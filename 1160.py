#População e taxa de crescimento
#cidade A e Cidade B
# Saber quantos anos levará para a cidade menor(sempre a A) ultrapassar a cidade B em população
# Fazer o cálculo apenas para as cidades cuja taxa de crescimento da cidade A é maior do que a da 
# cidade B 

#primeira entrada T sendo os casos de teste

#Cada caso de teste contem na mesma linha:
# PA e PB (indicando a população de cada cidade, onde 100 ≤ PA < 1000000, PA < PB ≤ 1000000)
# G1 e G2 (0.1 ≤ G1 ≤ 10.0, 0.0 ≤ G2 ≤ 10.0, G2 < G1)
# (Indicando o crescimento populacional de A e B (em percentual))

'''
Atenção: 
A população é sempre um valor inteiro, portanto, um crescimento de 2.5 % 
sobre uma população de 100 pessoas resultará em 102 pessoas, e não 102.5 pessoas, 
enquanto um crescimento de 2.5% sobre uma população de 1000 pessoas resultará em 1025 pessoas. 
Além disso, não utilize variáveis de precisão simples para as taxas de crescimento.
'''

#Saída
# Imprimir para cada caso de teste quantos anos levará para a cidade A passar a B em habitantes
# Se o tempo for maior que 100 anos o programa deve mostrar: 'Mais que 1 seculo'.

#Se o programa passar de 100 anos interrompo na hora

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
            message = 'Mais que 1 seculo'
            break
        else:
            message = f'{soma} anos.'
    print(message)



