# generae a cube of fabonacci series using map function

cube = lambda x: x*x*x

def fibonacci(n):
    l = []
    if n < 0:
        print("invalid entry")
    elif n == 1:
        l.append(0)
    elif (n >= 2) and (n <= 15) :
        a = 0
        b = 1

        for i in range(n):
            l.append(a)
            i = a + b
            a = b
            b = i

    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))