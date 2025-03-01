N,R = map(int, input().split())
for i in range(N):
    D, A = map(int, input().split())
    if D == 1 and 1600 <= R <= 2799:
        R = R + A
        continue
    if D == 2 and 1200 <= R <= 2399:
        R = R + A
        continue
print(R)