# 2304_창고다각형_warehouse-Polygon
import sys
input = sys.stdin.readline

N = int(input())

ans = 0

rect = []

cursor = 0
height = 0
max_h = 0
max_h_idx = 0

for _ in range(N):
    L, H = map(int, input().rstrip().split())
    if H >= max_h:
        max_h = H
        max_h_idx = L
    rect.append([L, H])

rect.sort(key=lambda x: x[0])


idx = 0
while height != max_h:
    l, h = rect[idx][0], rect[idx][1]
    if h > height:
        ans += height*(l-cursor)
        cursor = l
        height = h
        idx += 1
    else:
        idx += 1

if cursor != max_h_idx:
    ans += max_h*(max_h_idx - cursor + 1)
else:
    ans += max_h

idx = N-1
height = 0
cursor = 0
while height != max_h:
    l, h = rect[idx][0], rect[idx][1]
    if h > height:
        ans += height * (cursor - l)
        cursor = l
        height = h
        idx -= 1
    else:
        idx -= 1

print(ans)
