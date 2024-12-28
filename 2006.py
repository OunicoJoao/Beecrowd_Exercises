
if __name__ == '__main__':
    T = input()
    respsota = list(input().split())
    soma = 0
    for e in respsota:
        if e == T:
            soma += 1
    
    print(soma)
