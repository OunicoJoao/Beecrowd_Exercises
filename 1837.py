
if __name__ == '__main__':
    a,b = map(int,input().split())
    
    q = (b * (a // abs(b)) + (a % abs(b))) // abs(b)
    r = (b * (a // abs(b)) + (a % abs(b))) % abs(b)

    print(f'{q} {r}')
