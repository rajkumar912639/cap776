import array as arr
numer = arr.array('i',[2,3,4,5,6,7,8,9,5,3,7])
print(numer[:])
numer[3]=23
print(numer[:])
numer[3:6] =arr.array('i',[-3,-5,-6,-8])
print(numer[:])