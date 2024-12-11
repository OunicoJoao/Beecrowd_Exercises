#ler o tempo de viajem
temp = int(input())

#ler velocidade do carro
velo = int(input())

#(multiplicar tempo pela velocidade) e dividir por 12
gasto = (temp * velo) / 12

#printar gasolina gasta com tres casas depois da vírgula
print('{:.3f}'.format(gasto))