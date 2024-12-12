
def criptografar_LC(array):
   
   for element in array:
        word = ''.join([chr(ord(c) + 3) if c.isalpha() == True else c for c in element])

        word = word[::-1]

        metade = len(element) // 2
        cript = word[:metade] + ''.join([chr(ord(w) - 1) for w in word[metade:]])

        print(cript)

if __name__ == '__main__':
    quanti = int(input())
    vet = []
    for i in range(quanti):
        vet.append(input())
    criptografar_LC(vet)