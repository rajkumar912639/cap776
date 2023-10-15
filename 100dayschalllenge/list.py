
mylist = ["iphone","Apple","mi","savmsung","realme","oppo","xiomi","Oneplus",34,56]
print("mylist content are: ",mylist)
#list with difference item
print("All the item using loop")
for item in mylist:
    print(item)
#acess item using index no
print("index item is :",mylist[3])
#print elemnt using range
print("print using range",mylist[:3])
#negative index is
print("the negative index :",mylist[-3])
#append the element in the list
mylist.append("Raj")
print("The new list is",mylist)
#length of the list is
print("length of the list is",len(mylist))
# Insert the element in the list 
mylist.insert(3,"Motorola")
print("the new list is ",mylist)
#Remove the element from the list is
mylist.remove("Raj")
print("the new list is ",mylist)
#delet the element using index number
mylist.pop(-2)
print("the new list is :",mylist)
#delet the list using keyword delete
#del mylist
print("empty list is",mylist)
#searching in the list 
if "oppo" in mylist:
    print("Element is found ")
else:
    ("Element is not found")
#copy the list 
mylist2 = mylist.copy()
print("the new list is ",mylist2)
#reverse the list
mylist.reverse()
print("reverse the list is ",mylist)
mylist.append("oppo")
mylist.append("oppo")
#print the new list
print("the new list is",mylist)
# the no of times occur oppo
n=mylist.count("oppo")
print("how many time oppo occur in list",n)
#sort the list in increasing order
mylist.remove(56)
mylist.sort()
print("print the sorted list",mylist)
#the list is sort in reverse order
mylist.sort(reverse=True)
print("Reverse list in sorted form :",mylist)