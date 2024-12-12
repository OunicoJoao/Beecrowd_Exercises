

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