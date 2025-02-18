

if __name__ == '__main__':
    SENHA = 2002
    while True:
        tentativa = int(input())
        if tentativa == SENHA:
            print('Acesso Permitido')
            break
        else:
            print('Senha Invalida')