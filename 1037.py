#Acepted

num = float(input())

 #Intervalo [0,25] maior ou igual a 0 e menor ou igual 25
if num >= 0 and num <=25:
    print("Intervalo [0,25]") 

 #Intervalo (25,50] maior que vinte cinco e menor ou igual a 50
elif num >25 and num<=50:
    print("Intervalo (25,50]")

 #Intervalo (50,75] maior que 50 e menor ou igual a 75
elif num >50 and num <=75:
    print("Intervalo (50,75]")

 #Intervalo (75,100]) maior que 75 e menor ou igual a 100.
elif num > 75 and num <= 100:
    print("Intervalo (75,100]")
 #Fora de intervalo
else:
    print("Fora de intervalo")
 