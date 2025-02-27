def replace_wa_ac(S:str)->str:
    while "WA" in S:
        S=S.replace("WA","AC")
    return S

S=input().strip()
result = replace_wa_ac(S)
print(result) 