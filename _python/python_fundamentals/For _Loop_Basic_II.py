def bigone(arr):
    for i in range (0,len(arr)-1):
        if arr[i] > 0:
          arr[i] = 'big'
    return arr


num1 = [1,1,0,2,0]
num2 = [1,1,2,3,4]
print(bigone(num1))





