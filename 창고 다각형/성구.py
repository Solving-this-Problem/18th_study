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