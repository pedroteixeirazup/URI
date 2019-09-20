while True:
    string = input()

    if string == '*':
        break

    dataSplit = string.split(" ")
    flag = 0
    if len(dataSplit) == 1:
        flag = 1
    
    else:

        for i  in range(len(dataSplit)-1):
            if (dataSplit[0][:1].lower() == dataSplit[i+1][:1].lower() and dataSplit[0][:1].lower()):
                flag = 1
            else: 
                flag = 0
                break

        # print(flag)
       
    if flag == 1:
        print("Y", end='\n')
    else: 
        print("N", end='\n')
