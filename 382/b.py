N,D=map(int,input().split())
S=input()
for i in range(D):
    for j in range(N):
        if S[n-1-j]=='@':
            S=S[:n-1-j]+"."+S[n-j:]
            break
print(S)