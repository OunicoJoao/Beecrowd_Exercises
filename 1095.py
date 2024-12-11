#i -> 1, 4, 7, 10
#j -> 60, 55, 50, 45

if __name__ == '__main__':
    j = 60
    i = 1
    while j >= 0:
        print(f'I={i} J={j}')
        j -= 5
        i += 3
