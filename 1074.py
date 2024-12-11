
# Ler input de vezes para repetir

#Agora, no loop que rodará o numero de vezes definido anteriormente
#leio um valor e transformo em int e checo:
#se é par (EVEN em ingles), dividindo o valor por 2 e verificando se o resto é igual a zero
#se é ímpar (ODD), se o resto da divisão por 2 não for igual a zero
#ver se é positivo (POSITIVE), maior que zero
#se é negativo (NEGATIVE), menor que zero
#se for igual  zero (NULL)

#conforme a verificação devo imprimir na tela algum dos
# textos em parênteses acima.

repet = int(input())
lista = []

for i in range(repet):
    value = int(input())
    test = int(value % 2)
    if test == 0 and value > 0: #Par e positivo
        lista.append("EVEN POSITIVE")
    elif test != 0 and value > 0:
        lista.append("ODD POSITIVE")
    elif test == 0 and value < 0: #Par e positivo
        lista.append("EVEN NEGATIVE")
    elif test != 0 and value < 0:
        lista.append("ODD NEGATIVE")
    else:
        lista.append("NULL")

for i in lista:
    print(i)