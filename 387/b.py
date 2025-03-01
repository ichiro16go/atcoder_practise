X=int(input())
summ=0

for i in range(1, 10):
    for j in  range(1, 10):
        if i*j != X:
            summ+=i*j
print(summ)