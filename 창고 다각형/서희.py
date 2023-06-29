N = int(input())
arr = [0]*1001 

max_L = 0
max_H = 0
max_H_idx = 0

for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    if max_H < H:
        max_H = H
        max_H_idx = L
    max_L = max(max_L, L)

area = 0
temp_H = 0


for i in range(max_H_idx+1):
    if arr[i] > temp_H:
        temp_H = arr[i]
    area += temp_H

temp_H = 0


for i in range(max_L, max_H_idx, -1):
    if arr[i] > temp_H:
        temp_H = arr[i]
    area += temp_H

print(area)
