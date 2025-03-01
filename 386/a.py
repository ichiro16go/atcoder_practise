from collections import Counter

# 4枚のカードの整数を受け取る
A, B, C, D = map(int, input().split())

# 1枚カードを加えた時にフルハウスが成立するか判定
cards = [A, B, C, D]

# カードの出現回数をカウント
counter = Counter(cards)

# もしフルハウスを作れるなら
def can_make_full_house(counter):
    # 出現回数が3つのカードと2つのカードがあればフルハウス
    counts = sorted(counter.values())  # 出現回数をソート
    return counts == [2, 3]  # 2枚のカードが1種類と3枚のカードが1種類

# 1枚追加してフルハウスが作れるかチェック
for i in range(1, 14):  # 1～13の整数を1枚加える
    new_counter = counter.copy()
    new_counter[i] += 1  # カードiを追加
    if can_make_full_house(new_counter):
        print("Yes")
        break
else:
    print("No")
