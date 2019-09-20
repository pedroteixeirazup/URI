while True:
    tr = input()
    data = tr.split(' ')

    if data[0] == '0' and data[1] == '0':
        break

    aux = data[1]
    replaced = aux.replace(data[0],'')


    if replaced:
        intReplaced = int(replaced)
    else:
        intReplaced = 0

    print(intReplaced)

