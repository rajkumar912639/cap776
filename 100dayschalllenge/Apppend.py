import array as arr
arran = arr.array('i',[10,20,30,40])
print("Array element are : ")
print(arran)
arran.append(50)
print("Array element after append")
print(arran)
#add element at index2 is 
arran.insert(2,25)
print(arran)
#Remove element from the array i 20
arran.remove(20)
print(arran)#first add the element 
arran.append(55)
print(arran)
#pop or delete using index number
arran.pop(1)
print(arran)
#Reversee the array 
arran.reverse()
print(arran)
#reverse using index 
arrana =arran[::-1]
print(arrana)