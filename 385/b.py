H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1

S = []
for _ in range(H):
    S.append(list(input()))

T = input()

visited_houses = set()

for move in T:
    if move == 'U':
        if S[X-1][Y] == '.':
            X -= 1
        elif S[X-1][Y] == '@':
            X -= 1
            visited_houses.add((X, Y))
    elif move == 'D':
        if S[X+1][Y] == '.':
            X += 1
        elif S[X+1][Y] == '@':
            X += 1
            visited_houses.add((X, Y))
    elif move == 'L':
        if S[X][Y-1] == '.':
            Y -= 1
        elif S[X][Y-1] == '@':
            Y -= 1
            visited_houses.add((X, Y))
    elif move == 'R':
        if S[X][Y+1] == '.':
            Y += 1
        elif S[X][Y+1] == '@':
            Y += 1
            visited_houses.add((X, Y))

print(X + 1, Y + 1, len(visited_houses))