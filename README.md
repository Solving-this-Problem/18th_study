# 18th_study
[18주차] 코딩테스트 준비 6주차


[백준 문제집](https://www.acmicpc.net/workbook/view/15943)

# 쿠키의 신체 측정

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./%EC%BF%A0%ED%82%A4%EC%9D%98%20%EC%8B%A0%EC%B2%B4%20%EC%B8%A1%EC%A0%95/%EB%8F%99%EC%9A%B0.py)
```py
import sys
input = sys.stdin.readline

N = int(input())
arr = [input().strip() for _ in range(N)]

h_i, h_j = 0, 0                     # 심장 위치 찾기
for i in range(N):
    if h_i and h_j:                 # 머리를 찾으면 멈춰
        break
    for j in range(N):
        if arr[i][j] == '*':
            h_i, h_j = i + 1, j     # 심장 위치
            break

l_a, r_a, w, l_l, r_l = 0, 0, 0, 0, 0       # 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리 선언 및 초기화
for l_a_j in range(h_j - 1, -1, -1):        # 심장을 기준으로 하나씩 왼쪽으로 이동
    if arr[h_i][l_a_j] != '*':              # 신체 부위가 아니면 멈춰
        break
    l_a += 1

for r_a_j in range(h_j + 1, N):             # 심장을 기준으로 한나씩 오른쪽으로 이동
    if arr[h_i][r_a_j] != '*':
        break
    r_a += 1

for w_i in range(h_i + 1, N):               # 심장을 기준으로 하나씩 아래로 이동
    if arr[w_i][h_j] != '*':
        break
    w += 1

for l_l_i in range(h_i + w + 1, N):         # 허리가 끝나는 부분을 기준으로 하나씩 아래로 이동
    if arr[l_l_i][h_j - 1] != '*':          # 왼쪽 다리. 허리 기준 -1
        break
    l_l += 1

for l_l_i in range(h_i + w + 1, N):
    if arr[l_l_i][h_j + 1] != '*':          # 오른쪽 다리. 허리 기준 +1
        break
    r_l += 1

print(h_i + 1, h_j + 1)
print(l_a, r_a, w, l_l, r_l)
```

## [민웅](./%EC%BF%A0%ED%82%A4%EC%9D%98%20%EC%8B%A0%EC%B2%B4%20%EC%B8%A1%EC%A0%95/%EB%AF%BC%EC%9B%85.py)
```py
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
```

## [서희](./%EC%BF%A0%ED%82%A4%EC%9D%98%20%EC%8B%A0%EC%B2%B4%20%EC%B8%A1%EC%A0%95/%EC%84%9C%ED%9D%AC.py)
```py
N = int(input())

pattern = []
for _ in range(N):
    pattern.append(list(input()))

# 1. Find the head
for i in range(N):
    for j in range(N):
        if pattern[i][j] == "*":
            head = (i, j)
            break
    else:
        continue
    break


heart = (head[0] + 1, head[1])

l_arm, r_arm, waist, l_leg, r_leg = 0, 0, 0, 0, 0
i, j = heart

while  j-1-l_arm >= 0 and pattern[i][j-1-l_arm] == '*':
    l_arm += 1

while j+1+r_arm < N and  pattern[i][j+1+r_arm] == '*':
    r_arm += 1

while i+1+waist < N and  pattern[i+1+waist][j] == '*':
    waist += 1

while i+1+waist+l_leg < N and pattern[i+1+waist+l_leg][j-1] == '*':
    l_leg += 1

while i+1+waist+r_leg < N and pattern[i+1+waist+r_leg][j+1] == '*':
    r_leg += 1

print(*map(lambda x: x+1, heart)) 
print(l_arm, r_arm, waist, l_leg, r_leg)

```

## [성구](./%EC%BF%A0%ED%82%A4%EC%9D%98%20%EC%8B%A0%EC%B2%B4%20%EC%B8%A1%EC%A0%95/%EC%84%B1%EA%B5%AC.py)
```py
# 20125 쿠키의 신체 측정
import sys
input = sys.stdin.readline

N = int(input())
plate = [input().strip() for _ in range(N)]

# 심장
def searchHeart():
    for i in range(N):
        for j in range(N):
            if plate[i][j] == "*":
                return i+1, j

def length_of(heart):
    y, x = heart
    length = [0, 0, 0, 0, 0]
    # 왼쪽 팔    
    for i in range(x+1):
        if plate[y][i] == "*":
            length[0] = x - i 
            break
    # 오른쪽 팔
    for i in range(N-1, x,-1):
        if plate[y][i] == "*":
            length[1] = i - x
            break
    # 허리
    for i in range(1,N):
        if plate[y+i][x] == "_":
            break
        else:
            length[2] += 1
    # 왼쪽 다리
    for i in range(1,N):
        if y+length[2]+i>=N or plate[y+length[2]+i][x-1] == "_":
            break
        else:
            length[3] += 1
    # 오른쪽 다리
    for i in range(1,N):
        if y+length[2]+i>=N or plate[y+length[2]+i][x+1] == "_":
            break
        else:
            length[4] += 1
    return length
heart = searchHeart()
print(heart[0] +1, heart[1]+1)
print(*length_of(heart))
```

## [혜진](./%EC%BF%A0%ED%82%A4%EC%9D%98%20%EC%8B%A0%EC%B2%B4%20%EC%B8%A1%EC%A0%95/%ED%98%9C%EC%A7%84.py)
```py

N = int(input())
cookie = []
for _ in range(N):
    cookie.append(input())

x, y = 0, 0
flag = 0
leftarm, leftleg, rightarm, rightleg, back= 0, 0, 0, 0, 0
# 심장 찾기
for i in range(N):
    for j in range(N):
        if cookie[i][j] == '*':
            x, y = i + 2, j + 1
            print(x, y)
            flag = 1
            break
    if flag:
        break
# 오른팔
for i in range(y - 1):
    if cookie[x-1][i] == '*':
        leftarm += 1
# 왼팔
for i in range(y, N):
    if cookie[x-1][i] == '*':
        rightarm += 1
# 허리
for i in range(x, N):
    if cookie[i][y-1] == '*':
        back += 1
    else:
        x = i
        break

# 오른 다리
for i in range(x - 1, N):
    if cookie[i][y - 2] == '*':
        leftleg += 1

for i in range(x-1, N):
    if cookie[i][y] == '*':
        rightleg += 1

print(leftarm, rightarm, back, leftleg, rightleg)
```

</div>
</details>

# 창고 다각형

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95/%EB%8F%99%EC%9A%B0.py)
```py
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
arr.sort()


maxX = arr[-1][0]                           # 창고 최대 가로 폭
maxY, maxIdx = 0, 0                         # 기둥 최대 높이와 위치
for i in range(N):
    if maxY < arr[i][1]:
        maxY, maxIdx = arr[i][1], arr[i][0]

tmp = [0] * (maxX + 1)
for x, y in arr:
    tmp[x] = y                              # 창고의 모든 기둥 적어두기

total, left, right = 0, 0, 0
for i in range(maxIdx + 1):                 # 최대 기둥 위치를 기준으로 왼쪽 넓이 구하기
    if tmp[i] > left:                       # 기존 기둥보다 높은 기둥이 생길 때마다 갱신해주기
        left = tmp[i]
    total += left                           # 기둥들 누적 합

for j in range(maxX, maxIdx, -1):           # 오른쪽 넓이 구하기
    if tmp[j] > right:
        right = tmp[j]
    total += right

print(total)
```

## [민웅](./%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95/%EB%AF%BC%EC%9B%85.py)
```py
# 2304_창고다각형_warehouse-Polygon
# 오답이유 찾는중
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

```

## [서희](./%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95/%EC%84%9C%ED%9D%AC.py)
```py
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

```

## [성구](./%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95/%EC%84%B1%EA%B5%AC.py)
```py
# 2304 창고 다각형
import sys
import heapq
input = sys.stdin.readline

# 입력
N = int(input())
# 최대힙
storage = []
for _ in range(N):
    l, h = map(int, input().strip().split())
    heapq.heappush(storage,(-h, [l,h]))

# 기준이 되는 최대값 빼오기 위치, 길이
_, [Dlocation, Dheight] = heapq.heappop(storage)
# 최초 넓이(최대값의 길이에서 시작)
dimension = Dheight
# 왼쪽과 오른쪽을 나눔
left = Dlocation
right = Dlocation+1
# 최대값을 제외한 N-1번 반복
for _ in range(N-1):
    # 하나씩 빼오기(최대값순으로)
    _, [location, height] = heapq.heappop(storage)
    # 왼쪽에 있으면 넓이 구해서 더하기
    if location < left:
        dimension += (left - location) * height
        # 기준 초기화
        left = location
    # 오른쪽에 있으면 넓이 해서 더하기
    elif location >= right:
        dimension += (location+1 - right) * height
        # 기준 초기화
        right = location + 1
    # 그 외의 경우의 수는 넘어가기
# 결론 출력
print(dimension)
```

## [혜진](./%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95/%ED%98%9C%EC%A7%84.py)
```py
box = [0 for _ in range(1001)]
maxv = 0
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    box[a] = b
    if maxv < b:
        maxv = b
        max_idx = a

total, now = box[max_idx], 0
# total 누적합 / now 해당 인덱스의 값
maxV = 0

# 처음부터 최대 높이까지
for i in range(max_idx):
    if box[i]:
        if maxV < box[i]:
            maxV = box[i]
            now = box[i]
            total += now
        else:
            total += now
    else:
        total += now

# 맨 뒤에서 최대 높이까지
maxV, now = 0, 0
for i in range(1000,max_idx,-1):
    if box[i]:
        if maxV < box[i]:
            maxV = box[i]
            now = box[i]
            total += now
        else:
            total += now
    else:
        total += now

print(total)
```

</div>
</details>

# 불!

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./%EB%B6%88!/%EB%8F%99%EC%9A%B0.py)
```py
```

## [민웅](./%EB%B6%88!/%EB%AF%BC%EC%9B%85.py)
```py
# 4179_불_fire!
# 11% 틀렸습니다 원인 찾는중
import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

R, C = map(int, input().split())

maze = [list(map(str, input())) for _ in range(R)]

s = []
f = []
visited = [[-1]*C for _ in range(R)]
ans = 0
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            s = [i, j]
        elif maze[i][j] == 'F':
            f.append([i, j])
            visited[i][j] = 1
        elif maze[i][j] == '.':
            visited[i][j] = 0


q = deque()
for v in f:
    q.append(f.pop())

    while q:
        x, y = q.popleft()

        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx <= R-1 and 0 <= ny <= C-1:
                # 처음에 maze[nx][ny] == '.' 으로해서 J 위치 마킹못함
                if maze[nx][ny] != '#' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

s.append(0)
q.append(s)

visited2 = [[0]*C for _ in range(R)]
while q:
    x, y, dis = q.popleft()

    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx <= R-1 and 0 <= ny <= C-1:
            if (visited[nx][ny] >= dis+1 or visited[nx][ny] == 0) and visited2[nx][ny] == 0:
                visited2[nx][ny] = 1
                q.append([nx, ny, dis+1])
        else:
            ans = dis+1
            q = []
            break

if ans == 0:
    ans = 'IMPOSSIBLE'

print(ans)


```

## [서희](./%EB%B6%88!/%EC%84%9C%ED%9D%AC.py)
```py
```

## [성구](./%EB%B6%88!/%EC%84%B1%EA%B5%AC.py)
```py
# 4179 불!  -  불 먼저 돌리고 지훈이 돌리니 메모리 초과 따라서 턴마다 task 처리
# 질문게시판을 돌아보면서 풀었음..
import sys
from collections import deque
input = sys.stdin.readline

# 방향 리스트
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# 불과 지훈이 위치 찾기
def find_j_f():
    for i in range(R):
        for j in range(C):
            if maze[i][j] == "J":
                start.append(i)
                start.append(j)
            elif maze[i][j] == "F":
                fire.append((i, j))


def bfs(start_y, start_x):
    # 지훈이 용 큐
    jque = deque([(start_y, start_x)])
    # 불 용 큐
    fque = deque([])
    # 방문 확인
    visited = [[0]*C for _ in range(R)]
    # 불은 -1, 지훈이는 턴 수
    for idx in range(len(fire)):
        fque.append((fire[idx][0], fire[idx][1]))
        visited[fire[idx][0]][fire[idx][1]] = -1
    visited[start_y][start_x] = 1
    while jque:
        # print("TURN")
        # 지훈이와 불의큐 길이 만큼 반복문을 돌아 1분당 할일을 모두 하게 함
        flen = len(fque)
        jlen = len(jque)
        # 불 먼저
        for _ in range(flen):
            fi, fj = fque.popleft()
            for di, dj in dir:
                fni, fnj = fi+di, fj+dj
                # "." 확인 안해서 38% 틀림
                if 0<=fni<R and 0<=fnj<C and maze[fni][fnj] == '.' and not visited[fni][fnj]:
                    fque.append((fni, fnj))
                    visited[fni][fnj] = -1
        # 지훈이 차례
        for _ in range(jlen):
            ji, jj = jque.popleft()
            for jdi, jdj in dir:
                jni, jnj = ji+jdi, jj+jdj
                # 출구에 서있으면 멈춤
                if jni < 0 or jni >= R or jnj < 0 or jnj >= C:
                    # 턴수 출력
                    return visited[ji][jj]
                elif maze[jni][jnj] == "." and not visited[jni][jnj]:
                    jque.append((jni, jnj))
                    visited[jni][jnj] = visited[ji][jj] + 1
        # [print(visited[index]) for index in range(R)]
    # 다 돌았는데 없으면 "불가능"
    return "IMPOSSIBLE"
            

R, C = map(int, input().strip().split())
maze = [input().strip() for _ in range(R)]
# 불 위치
fire = []
# 지훈이 시작 위치
start = []
find_j_f()
print(bfs(start[0], start[1]))
```

## [혜진](./%EB%B6%88!/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>
