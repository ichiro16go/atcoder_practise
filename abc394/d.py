def is_colorful_bracket_sequence(S):
    stack = []
    matching_bracket = {')': '(', ']': '[', '>': '<'}
    
    for char in S:
        if char in '([<':
            stack.append(char)
        elif char in ')]>':
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return False
    return not stack

    S = input().strip()
    if is_colorful_bracket_sequence(S):
        print("Yes")
    else:
        print("No")