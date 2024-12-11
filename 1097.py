
if __name__ == '__main__':
    j = 7
    for i in range(1,10,2):
        b = 0
        a = j
        while b < 3:
            print(f'I={i} J={a}')
            a -= 1
            b+=1
        j += 2
