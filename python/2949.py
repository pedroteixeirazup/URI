n = int(input())
hobbit = 0
humano = 0
elfo = 0
anao = 0
mago = 0
while n :
    string = input()
    data = string.split(' ')


    if data[1] == 'X':
        hobbit = hobbit + 1
    elif data[1] == 'A':
        anao = anao + 1
    elif data[1] == 'E':
        elfo = elfo + 1
    elif data[1] == 'H':
        humano = humano + 1
    else:
        mago = mago + 1

    n = n - 1

print(str(hobbit) + ' Hobbit(s)')
print(str(humano) + ' Humano(s)')
print(str(elfo) + ' Elfo(s)')
print(str(anao) + ' Anao(s)')
print(str(mago) + ' Mago(s)')
