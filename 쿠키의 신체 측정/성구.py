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