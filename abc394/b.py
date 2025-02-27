import re

def concatenate_sorted_strings(strings):
    strings = [re.sub(r'\d', '', s) for s in strings]
    # 文字列を長さの昇順にソート
    sorted_strings = sorted(strings, key=len)
    # ソートされた文字列を結合
    result = ''.join(sorted_strings)
    return result


# 関数の呼び出し
strings=input().strip().split()
result = concatenate_sorted_strings(strings)
print(result)  # 出力例: "aababc"