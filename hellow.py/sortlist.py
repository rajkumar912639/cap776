mylist =["iphone","Mi","Apple","vivo","savmsung","Oneplus"]
print("unsorted list",mylist)
def findlen(e):
    return len(e)
mylist.sort(key=findlen)
print("sorted list increement order  ")
print('\n',mylist)
mylist.sort(reverse=True,key=findlen)
print("\n sorted list in decrement order :",mylist)

