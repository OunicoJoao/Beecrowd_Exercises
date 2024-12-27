def calc_carneiros(vet_sitios):
    vet_aux = vet_sitios
    index = 0
    sitios_atacados = 1

    while True:
        if index < 0 or index > len(vet_sitios) - 1:
            break
        atual = vet_aux[index]
        if index + 1 > sitios_atacados: sitios_atacados = index + 1

        if atual % 2 == 0: #par
            if vet_aux[index] > 0: vet_aux[index] -= 1
            index -= 1
        elif atual % 2 == 1: #impar
            if vet_aux[index] > 0: vet_aux[index] -= 1
            index += 1
            
    print(f'{sitios_atacados} {sum(vet_aux)}')

if __name__ == '__main__':
    N = int(input())
    sitios = [int(i) for i in input().split( )]
    calc_carneiros(sitios)
    
    