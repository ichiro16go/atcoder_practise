S = input()

count = 0
index = 0

while index < len(S):
    if S[index] == "0" and index + 1 < len(S) and S[index + 1] == "0":
        # "00"のとき
        count += 1
        index += 2
    else:
        # 普通の数字のとき
        count += 1
        index += 1

print(count)
