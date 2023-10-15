numlist =[3,45,53,56,35,34,6,4,64,344,34,34,34,32]
print("list of the number is \n ",numlist)
searchnum =int(input("Ente the number to search : "))
found =False
for i in range (len(numlist)):
    if numlist[i]==searchnum:
        found =True
        print(searchnum,"The number is found in the list at index no : ",i)
        break
if found==False:
    print(searchnum,"number is not found in the list")