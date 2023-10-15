import array as arr
numA =arr.array('i',[13,34,34])
numB =arr.array('i',[45,46,48])
print(numA)
numA.extend(numB)
print(numA)
#add two array using concatination
numc=numA+numB
print(numc)
#number occurance in the list
n=numc.count(45)
print("the specific number occur :",n)