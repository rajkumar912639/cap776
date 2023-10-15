var = [2,3,4,5,6,4,63,45]
a = sum(var)
print(a)
m = var[0]
for i in var[1: ]:
    if(m<i):
        m=i
print(" greatest number",m)
//next program
lst=[ 1, 6, 3, 5, 3, 4 ]

i=7

if i in lst:
    print("exist")
else:
    print("not exist")
//prime number
l1 = [2, 3, 4, 56, 45, 35, 43, 56, 75, 34, 67, 45, 59, 34, 23]
c = 0
for i in l1:
    f = 0
    for j in range(2, i):
        if i % j == 0:
            f = 1
            break
    if f == 0:
        c += 1
        print("prime no =", i)
print("total prime no =", c)
//vovels of string
c = 0
name = " RAJKUMAR"
v = ['A', 'E', 'I', 'O', 'U']
for i in name:
    if i in v:
        c += 1
        print(i)
print("total =", c)
//list program


