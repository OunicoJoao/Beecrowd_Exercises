
if __name__ == '__main__':
    a,b = map(int,input().split())
    
    q = (b * (a // abs(b)) + (a % abs(b))) // abs(b)
    r = (b * (a // abs(b)) + (a % abs(b))) % abs(b)

    print(f'{q} {r}')

"""
if __name__ == '__main__':
    a, b = map(int, input().split())

    q = a // b  # Cálculo inicial do quociente
    r = a % b   # Cálculo inicial do resto

    # Ajustar o quociente e o resto para garantir 0 ≤ r < |b|
    if r < 0:
        q += 1 if b < 0 else -1  # Ajusta q para cima se b < 0, para baixo se b > 0
        r += abs(b)

    print(q, r)
"""