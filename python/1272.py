n = int(input())

while n != 0:
    str = input()

    data = str.split(' ')

    aux = ''

    for i in range(len(data)):
        aux += data[i][:1]

    print(aux)

    n = n-1
