

if __name__ == '__main__':

    cobaias = {'C': 0, 'R': 0,'S': 0}
    total = 0
    counter = int(input())
    i = 0
    while i < counter:
        linha = [i for i in input().split()]
        
        cobaias[linha[1]] += int(linha[0])
        total += int(linha[0])
        i += 1
    
    #Descobrindo o percentual
    perC = (cobaias['C'] * 100) / total
    perR = (cobaias['R'] * 100) / total
    perS = (cobaias['S'] * 100) / total

    #imprimindo:
    print(f'Total: {total} cobaias')
    print(f'Total de coelhos: {cobaias["C"]}')
    print(f'Total de ratos: {cobaias["R"]}')
    print(f'Total de sapos: {cobaias["S"]}')
    print(f'Percentual de coelhos: {perC:.2f} %')
    print(f'Percentual de ratos: {perR:.2f} %')
    print(f'Percentual de sapos: {perS:.2F} %')
    