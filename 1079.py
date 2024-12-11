
N = int(input(""))
c = N
resul = []
while N > 0:
    seq = input()
    seq = seq.split()
    num1 = float(seq[0])
    num2 = float(seq[1])
    num3 = float(seq[2])
    mediaP = round(2 * num1 + 3* num2 + 5 * num3) / 10
    resul.append(mediaP)
    N-=1

for i in range(c):
    print(resul[i])





