
n = int(input())

for i in range(10000):
    rest = i % n
    if rest == 2:
        print(i)
        
