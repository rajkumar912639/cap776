for x in range(1,6):
    for y in range(1,6):
        print("*",end="")
    print()
#print the number on place of *
for x in range(1,6):
    for y in range(1,6):
        print(x,end="")
    print()
#print the anothe pttern
for x in range(1,6):
    for y in range(1,6):
        print(y,end="")
    print()
#print the pattern in opposite
for x in range(5,0,-1):
    for y in range(5,0,-1):
        print(x,end="")
    print()
#print anothe sequance after that
for x in range(5,0,-1):
    for y in range(5,0,-1):
        print(y,end="")
    print()
#print the element in sequance in matrics
n=5
k=1
for x in range(1,n+1):
    for y in range(1,n+1):
        print("{:4d}".format(k),end="")
        k+=1
    print()
# only prin the odd element
n=5
k=1
for x in range(1,n+1):
    for y in range(1,n+1):
        print("{:4d}".format(k),end="")
        k+=2
    print()
print(" the table of 5")
n=5
k=5
for x in range(1,n+1):
    for y in range(1,n+1):
        print("{:4d}".format(k),end="")
        k+=5
    print()
print("print the serial number row ")
n=5
for x in range (1,n+1):
    for y in range (1,n+1):
        print("{:4d}".format(x),end="")
        x+=n
    print()
print("print the serial number column ")
n=5
for x in range (1,n+1):
    for y in range (1,n+1):
        print("{:4d}".format(y),end="")
        y+=n
    print()
#pattern 13 2nd day codding of python re
    