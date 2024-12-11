
n = 1
maior = 0
posição = 0
while n <= 100:
    num = float(input(""))
    if num > maior:
        maior = num
        posição = n
    n+=1

print("{:.0f}".format(maior))
print(posição)