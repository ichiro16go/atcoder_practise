# Read three integers from input
A, B, C = map(int, input().split())

# Check if the sum of any two numbers equals the third number
if A + B == C:
    print("Yes")
elif A == B + C:
    print("Yes")
elif B == A + C:
    print("Yes")
elif A==B==C:
    print("Yes")
else:
    print("No")