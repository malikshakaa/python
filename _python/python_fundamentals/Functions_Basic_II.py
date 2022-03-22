def countdown(x):
    num_list = [ ]
    for i in range (x,0,-1):
        num_list.append(i)
    return num_list 
print(countdown(5))


def printreturn(a,b):
    print(a)
    return b
c=printreturn(1,2)
print(c)


mylist=[1,2,3]
def x(arr):
    return arr[0] + len(arr)
print(x(mylist))

def greater(arr):
    my_list=[ ]
    if len(arr)<2:
        print('false')
    else:
        for i in range (0,len(arr)):
            if arr[i]>arr[1]:
                my_list.append(arr[i])
        print(my_list)
        print(len(my_list))
greater([5,2,3,2,1,4])
greater([5])

def x (s,v):
    my_list = []
    for i in range (0,s):
        my_list.append(v)
    print(my_list)
x(5,7)
