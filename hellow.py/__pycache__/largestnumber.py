arr=[]
num =int(input("Enter the N numbers :  "))
for i in range (num):
    numbers =int(input(" enter the number :"))
    arr.append(numbers)
    print("maximum number is :",max(arr))
    print("minimun number is ",min(arr))
    