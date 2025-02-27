def is_1122_number_sequence(N:int,S:str)->bool:
    # st = extract_twos(S)
    st=S
    if N%2!=0:
        return False
    mid = N//2
    for i in range(mid):
        if st[2*i]!=st[2*i-1]:
            return False
    from collections import Counter
    count = Counter(st)
    for value in count.values():
        if value != 2:
            return False
    return True

def longest_1122_number_sequence(S:str)->int:
    max_length = 0
    N=len(S)
    for i in range(N):
        for j in range(i+1,N+1):
            if is_1122_number_sequence(j-i, S[i:j]):
                max_length = max(max_length, j - i)
    return max_length


N=int(input())
S=input().strip().replace(" ", "")
print(str(longest_1122_number_sequence(S)))
