#Estrela 1 é o proprio sítio e rouba 1

#se o sitio estrela i tem carneiro rouba 1

# e segue ou para no sitio i + 1 se o numero de carneiros em estrela i é impar
# ou volta para o sitio i - 1 se o numero de carneiros em estrela i é par

#Se precisar avançar para a estrela i + 1 e ela não existir, então paramos o programa

def calc_carneiros(vet_sitios):
    soma = sum(vet_sitios)
    vet_aux = vet_sitios
    i = 0
    carneiros = 0
    #Definindo o range que o i não pode passar de -N até N.
    while i != -len(vet_sitios) - 1 and i != len(vet_sitios) - 1:
        
        if vet_aux[i] > 0:
            carneiros += 1
            vet_aux[i] -= 1
        #impar
        if vet_aux[i] % 2 == 1:
            i += 1
        #par
        if vet_aux[i] % 2 == 0:
            i -= 1
        
    print(f'{carneiros} {soma - carneiros}')

if __name__ == '__main__':
    N = int(input())
    sitios = [int(i) for i in input().split( )]
    calc_carneiros(sitios)
    
    