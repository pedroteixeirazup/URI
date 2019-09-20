n = int(input())

while n != 0:
    str = input()
    aux = ''
    for i in str:
        if i.isdigit():
            aux+=i
        else:
            aux+='.'
    
    data = aux.split('.')
    summ = 0
    for i in range(len(data)):
        if data[i] != '':
            summ = summ + int(data[i])
  
    
    print(summ)
    n = n-1