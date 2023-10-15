mylist=[[2,3,4,5,23,34,34],[34,35,65,45,78,6,8,],[23,56,76,45,45,32,87]]
print("print the list",mylist)
#using loop print the element
for x in mylist:
    print(x)
#using iterate the list 
for x in mylist:
    for y in x:
        print(y)
        
#create a multidimensional array with zero
r=4
c=3
mlist=[[0 for x in range(r)]for x in range(c)]
print("all element in multidimensional arry")
print(mlist)
# append the sublist
mylist.append([23,34,56,57,78])
print("print the new list",mylist)
#reverse the list 
mylist.reverse()
print("print the reverse list",mylist)
#sort the list 
mylist.sort()
print("print the sorted list",mylist)
