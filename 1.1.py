def fun(a,b):
    table = []
    line = []
    for i in range(1,a+1):
        table = []
        for j in range(1,b+1):
            table.append(i*j)
        line.append(table)

    return line

for i in fun(3,4):
    print('')
    for j in i:
        print(j, end=" ")


