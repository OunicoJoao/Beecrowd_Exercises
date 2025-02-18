
if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    for num in range(min(X,Y) + 1,max(X,Y)):
        if num % 5 in (2,3):
            print(num)
