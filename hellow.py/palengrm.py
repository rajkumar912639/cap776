s1 = input("Enter main stream: ")
s2 = input("Enter the target stream: ")
f = 0  # Initialize 'f' to 0 before the loop

for i in s2:
    if i not in s1:  # Missing colon here
        f = 1
        break

# Added a missing colon in the following line
if f == 0 and len(s1) == len(s2):  
    print("Anagram")
else:
    print("Not anagram")
