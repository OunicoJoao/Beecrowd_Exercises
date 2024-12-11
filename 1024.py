def criptografar(array):
   
   for element in array:
        word = ''
        for c in element:
            if c.isalpha() == True:
                word += chr(ord(c) + 3)
            else:
                word += c

        word = word[::-1]

        metade = len(element) // 2
        cript = word[:metade]
        for w in word[metade:]:
            cript += chr(ord(w) - 1)

        print(cript)

#OU utilizando list comprehension
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
    criptografar(vet)
    criptografar_LC(vet)