def extract_twos(S:str)->str:
    return"".join(c for c in S if c=="2")

S=input().strip()
print(extract_twos(S))