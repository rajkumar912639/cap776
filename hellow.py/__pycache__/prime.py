count =0
n=int(input("Enter the numbe is :"))
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("the number is prime number ")
else:
     print("is not prime number")