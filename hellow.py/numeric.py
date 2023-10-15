emp=[('alice','e001','Manager',600000),
     ('raj','e002','Manager',700000),
     ('Rao','e003','Managerr',56000)]
sum=0
for i in emp:
    for j in i:
        if j.isnumeric:
            sum +=j
print(sum)
