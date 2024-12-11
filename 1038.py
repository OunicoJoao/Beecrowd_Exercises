valores = [{'cod': 1, 'preco': 4.0},
           {'cod': 2, 'preco': 4.5},
           {'cod': 3, 'preco': 5.0},
           {'cod': 4, 'preco': 2.0},
           {'cod': 5, 'preco': 1.5}]

#dois inputs codigo e quantidade
texto = input()

codigo = int(texto[0]) 
quantidade = int(texto[2])

#print o total 
#acessar preço apartir do codigo e multiplicar por quantidade

for elemento in valores:

    if elemento['cod'] == codigo:
        soma = elemento['preco'] * quantidade
        print(f'Total: R$ {soma:.2f}')    