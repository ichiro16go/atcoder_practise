def is_1122_bracket(S: str) -> str:
    n = len(S)
    if n % 2 != 0:
        return "No"
    
    for i in range(n // 2):
        if S[2 * i] != S[2 * i + 1]:
            return "No"
    
    from collections import Counter
    count = Counter(S)
    for value in count.values():
        if value != 2:
            return "No"
    
    return "Yes"

S=input().strip()
print(is_1122_bracket(S))