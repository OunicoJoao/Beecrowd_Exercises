
if __name__ == '__main__':
    lista = []
    while True:
        D,N = input().split()
        if D == '0' and N == '0':
            break
            
        new_num = ''
        for digit in N:
            if digit != D:
                new_num += digit
        lista.append(new_num)
    for num in lista:
        print(int(num) if num != '' else 0)