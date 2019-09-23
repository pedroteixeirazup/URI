n = int(input())

while n:
    string = input()
    counterA = 0
    counterB = 0
    counterC = 0
    counterD = 0
    counterE = 0
    counterF = 0
    counterG = 0
    counterH = 0
    counterI = 0
    counterJ = 0
    counterK = 0
    counterL = 0
    counterM = 0
    counterN = 0
    counterO = 0
    counterP = 0
    counterQ = 0
    counterR = 0
    counterS = 0
    counterT = 0
    counterU = 0
    counterV = 0
    counterW = 0
    counterX = 0
    counterY = 0
    counterZ = 0
    dic = {'a':0 ,'b':0 ,'c':0 ,'d':0 ,'e':0 ,'f':0 ,'g':0 ,'h':0 ,'i':0 ,'j':0 ,'k':0 ,'l':0 
    ,'m':0 ,'n':0 ,'o':0 ,'p':0 ,'q':0 ,'r':0 ,'s':0 ,'t':0 ,'u':0 ,'v':0 ,'w':0 ,'x':0 ,'y':0 ,'z':0 }

    for letter in string:
        # if letter.isalpha():
            if letter.lower() == 'a':
                counterA = counterA + 1
                dic['a'] = counterA
            if letter.lower() == 'b':
                counterB = counterB + 1
                dic['b'] = counterB
            if letter.lower() == 'c':
                counterC = counterC + 1
                dic['c'] = counterC
            if letter.lower() == 'd':
                counterD = counterD + 1
                dic['d'] = counterD
            if letter.lower() == 'e':
                counterE = counterE + 1
                dic['e'] = counterE
            if letter.lower() == 'f':
                counterF = counterF + 1
                dic['f'] = counterF
            if letter.lower() == 'g':
                counterG = counterG + 1
                dic['g'] = counterG
            if letter.lower() == 'h':
                counterH = counterH + 1
                dic['h'] = counterH
            if letter.lower() == 'i':
                counterI = counterI + 1
                dic['i'] = counterI
            if letter.lower() == 'j':
                counterJ = counterJ + 1
                dic['j'] = counterJ
            if letter.lower() == 'k':
                counterK = counterK + 1
                dic['k'] = counterK
            if letter.lower() == 'l':
                counterL = counterL + 1
                dic['l'] = counterL
            if letter.lower() == 'm':
                counterM = counterM + 1
                dic['m'] = counterM
            if letter.lower() == 'n':
                counterN = counterN + 1
                dic['n'] = counterN
            if letter.lower() == 'o':
                counterO = counterO + 1
                dic['o'] = counterO
            if letter.lower() == 'p':
                counterP = counterP + 1
                dic['p'] = counterP
            if letter.lower() == 'q':
                counterQ = counterQ + 1
                dic['q'] = counterQ
            if letter.lower() == 'r':
                counterR =  counterR + 1
                dic['r'] = counterR
            if letter.lower() == 's':
                counterS = counterS + 1
                dic['s'] = counterS
            if letter.lower() == 't':
                counterT = counterT + 1
                dic['t'] = counterT
            if letter.lower() == 'u':
                counterU = counterU + 1
                dic['u'] = counterU
            if letter.lower() == 'v':
                counterV = counterV + 1
                dic['v'] = counterV
            if letter.lower() == 'x':
                counterX = counterX + 1
                dic['x'] = counterX
            if letter.lower() == 'z':
                counterZ = counterZ + 1
                dic['z'] = counterZ
            if letter.lower() == 'y':
                counterY = counterY + 1
                dic['y'] = counterY
            if letter.lower() == 'w':
                counterW = counterW + 1
                dic['w'] = counterW


    maxValue = max(dic.values())
    auxS = ''

    for index in dic:
        if maxValue == dic[index]:
            auxS += index

    print(auxS)
    
    n = n - 1