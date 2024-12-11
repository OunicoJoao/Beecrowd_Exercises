
if __name__ == '__main__':
    i = 0
    while i <= 2:
        if i == int(i):
            i = int(i)
            for j in range(1,4):
                j += i
                print('I={} J={}'.format(i,j))
        else:
            for j in range(1,4):
                j += i
                print('I={:.1f} J={:.1f}'.format(i,j))
        i += 0.2
        i = round(i,1)
