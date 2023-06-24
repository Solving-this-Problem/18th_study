# 20125_쿠키의신체측정_Cookie
import sys
input = sys.stdin.readline

N = int(input())

field = [list(map(str, input())) for _ in range(N)]

heart = False
body_end = False
belly = 0
for i in range(N):
    for j in range(N):
        if field[i][j] == '*':
            heart = [i+2, j+1]
            nx, ny = i, j
            while field[nx][ny] == '*':
                nx += 1
                belly += 1
            body_end = [nx, ny]
            break
    if heart:
        break

[x, y] = heart
ans = []
cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
for i in range(y-1):
    if field[x-1][i] == '*':
        cnt1 += 1

for i in range(y, N):
    if field[x-1][i] == '*':
        cnt2 += 1

for i in range(body_end[0], N):
    if field[i][body_end[1]-1] == '*':
        cnt3 += 1

for i in range(body_end[0], N):
    if field[i][body_end[1]+1] == '*':
        cnt4 += 1
print(x, y)
print(cnt1, cnt2, belly-2, cnt3, cnt4)