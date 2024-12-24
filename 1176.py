#Resolver este problema

def func_fib(num):
    fib = [0,1]
    for i in range(1,num):
        fib.append(fib[i-1] + fib[i])
    return fib[num]

if __name__ == '__main__':
    count = int(input())
    n = []
    for _ in range(count):
        n.append(int(input()))
    
    for i in n:
        print(f'Fib({i}) = {func_fib(i)}')