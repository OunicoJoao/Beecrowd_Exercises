
if __name__ == '__main__':
    resul = []
    while True:
        M,N = map(int,input().split())
        if M <= 0 or N <= 0:
            break
        menor,maior = min(M,N),max(M,N)
        soma_intervalo = ((maior - menor + 1) * (menor + maior)) // 2 # formula para soma de um intervalo 
        sequencia = list(range(menor,maior+1))

        resul.append(" ".join(map(str, sequencia)) + f" Sum={soma_intervalo}")
    
    print('\n'.join(resul))
        

