fruits ={"apple","banana",'grapes',"orange","mango",'cherry'}
print(fruits)
search =input("Enter the fruit you want to search in set : ")
if search in fruits:
    print("yes",search,'is in the set ')
else:
    print("Not in the set")