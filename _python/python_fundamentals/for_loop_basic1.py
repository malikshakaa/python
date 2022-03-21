def printint(x):
        for i in range (0,x):
            print(i)
printint(151)

def printmlt(y):
    for i in range (0,y):
        if(i%5==0):
            print(i)
printmlt(1001)


def dojo(z):
    for i in range (1,z):
        if(i%10==0):
            print('coding Dojo')
        if(i%5==0):
            print('coding')
        else:print(i)
dojo(101)


def oddprint(e):
    sum = 0
    for i in range(0,e):
        if(i%2==1):
            sum +=i 
            print(sum)
oddprint(10)

def Countdown(k):
    for i in range(k,0, -4):
        print(i)
Countdown(2018)



def flexiblecount(l,h,m):
    for i in range(l,h,m):
        print(i)
flexiblecount(2,9,3)





