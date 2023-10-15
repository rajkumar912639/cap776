mytuple = ("c++","python","java",'Fortran',"Js",34,56,67,34)
print(mytuple)
mytu =("Rajkumar")
print(mytu)
for x in mytuple :
    print(x)
    #acces the element using index number
print(mytuple[3])
#accces element using index number
print("element are:",mytuple[2:5])
#access element using negative index
print("negative index element is :",mytuple[-3])
#Tuple length is 
print("the length of tuple is:", len(mytuple))
#search the element in tuple
search=input("Enter the element in to search: ")
if search in mytuple :
    print(search ,"found the element in tuple")
else:
    print("not found ")
#concatenate the two tuple
#tupleA=mytuple+mytu
#print("the new tuple is :",tupleA)
n=mytuple.count(34)
print(n)