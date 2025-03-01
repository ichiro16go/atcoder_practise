H,W,D=map(int,input().split())
S=[]
for i in range(H):
    s=input()
    S.append(s)
C=[[0 for i in range(W)] for j in range(H)]
#距離がD以下か
def dis(x1,y1,x2,y2):
    return (D>=abs(x1-x2)+abs(y1-y2))
#床
P1=[]
for i in range(H):
    for j in range(W):
        if S[i][j]==".":
            P1.append((i,j))

N=len(P1)
ans= 0
for i in range(N):
    for j in range(N):
        ST=set()
        for i2 in range(N):
            #1台目の加湿器
            if(dis(P1[i][0],P1[i][1],P1[i2][0],P1[i2][1])):
                ST.add((P1[i2][0],P1[i2][1]))
            #2台目の加湿器
            if(dis(P1[j][0],P1[j][1],P1[i2][0],P1[i2][1])):
                ST.add((P1[i2][0],P1[i2][1]))
        ans=max(ans,len(ST))
print(ans)