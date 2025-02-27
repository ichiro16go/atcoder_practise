def is_11_22_bracket(S: str,N:int) -> str:
    n = N
    
    # Check if the length of S is odd
    if n % 2 == 0:
        return "No"
    
    mid = n // 2
    
    # Check if the first half (excluding the middle) is all '1's
    if not all(c == '1' for c in S[:mid]):
        return "No"
    
    # Check if the middle character is '/'
    if S[mid] != '/':
        return "No"
    
    # Check if the second half (excluding the middle) is all '2's
    if not all(c == '2' for c in S[mid+1:]):
        return "No"
    
    return "Yes"

def longest_11_22_substring(S:str)->str:
    max_length = 0
    n=len(S)
    for i in range(n):
        for j in range(i+1,n+1):
             if is_11_22_bracket(S[i:j], j - i) == "Yes":
                max_length = max(max_length, j - i)

    return str(max_length)
# Read input
N = int(input())
S = input()

# Determine if S is an "11/22" string and print the result
print(longest_11_22_substring(S))