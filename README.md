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
```

## [서희](./%EC%BF%A0%ED%82%A4%EC%9D%98%20%EC%8B%A0%EC%B2%B4%20%EC%B8%A1%EC%A0%95/%EC%84%9C%ED%9D%AC.py)
```py
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
```

</div>
</details>

# 창고 다각형

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95/%EB%8F%99%EC%9A%B0.py)
```py
```

## [민웅](./%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95/%EB%AF%BC%EC%9B%85.py)
```py
```

## [서희](./%EC%B0%BD%EA%B3%A0%20%EB%8B%A4%EA%B0%81%ED%98%95/%EC%84%9C%ED%9D%AC.py)
```py
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
```

## [서희](./%EB%B6%88!/%EC%84%9C%ED%9D%AC.py)
```py
```

## [성구](./%EB%B6%88!/%EC%84%B1%EA%B5%AC.py)
```py
```

## [혜진](./%EB%B6%88!/%ED%98%9C%EC%A7%84.py)
```py
```

</div>
</details>
