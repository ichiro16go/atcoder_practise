X = int(input())

N = 1
factorial = 1

while factorial < X:
    N += 1
    factorial *= N

if factorial == X:
    print(N)