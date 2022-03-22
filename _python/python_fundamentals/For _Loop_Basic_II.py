def bigone(arr):
    for i in range (0,len(arr)):
        if arr[i] > 0:
          arr[i] = 'big'
    return arr


num1 = [1,1,0,2,0]
num2 = [1,1,2,3,4]
print(bigone(num1))



def countpositive(arr):
    count = 0
    for i in range (0,len(arr)):
             if arr[i] > 0 :
                count+=1
    arr[len(arr)-1]=count
    print(arr)

countpositive([1,6,-4,-2,-7,-2])


def sumtotal(arr):
    sum =   0
    for i in range (0,len(arr)):
        sum += arr[i]
    print(sum)
    return(sum)
sumtotal([1,2,3,4])


def Average(arr):
    sum = 0
    avrg = 0
    for i in range (0,len(arr)):
        sum +=arr[i]
    avrg=(sum/len(arr))
    print(avrg)
    return(avrg)
Average([1,2,3,4])


def length(arr):
    l=len(arr)
    print(l)
    return(l)
length([1,1,1,1,1,])

def minimum(arr):
    min = 1000000000000000000000000000000000
    if len(arr) == 0:
        print('false')
    else:
        for i in range (0,len(arr)):
            if arr[i]<min:
                min = arr[i]
        print(min)
        return(min)
minimum([37,2,1,-9])
minimum([])



def maximum(arr):
    max = -1000000000000000000000000000000000
    if len(arr) == 0:
        print('false')
    else:
        for i in range (0,len(arr)):
            if arr[i]>max:
                max = arr[i]
        print(max)
        return(max)
maximum([37,2,1,-9])
maximum([])

def Ultimate_Analysis(arr):
    x ={'sumTotal':sumtotal(arr) ,
     'average': Average(arr),
      'minimum': minimum(arr),
       'maximum':maximum(arr),
        'length':length(arr)
        }
    print(x)
Ultimate_Analysis([37,2,1,-9])

def reverse_List(arr):
    first = 0
    last = len(arr)-1
    while first < last:
        temp = arr[first]
        arr[first]=arr[last]
        arr[last]= temp
        first+=1
        last-=1
    print(arr)
reverse_List([37,2,1,-9])

















