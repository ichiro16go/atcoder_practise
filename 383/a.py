N = int(input())
T = []
V = []

for _ in range(N):
    t, v = map(int, input().split())
    T.append(t)
    V.append(v)

current_water = 0
previous_time = 0

for i in range(N):
    # 経過時間
    dt = T[i] - previous_time
    # 水の減少
    current_water = max(0, current_water - dt)
    # 水の追加
    current_water += V[i]
    # 時刻を更新
    previous_time = T[i]

# 最後の時間までの減少
current_water = max(0, current_water - (T[-1] - previous_time))

print(current_water)
