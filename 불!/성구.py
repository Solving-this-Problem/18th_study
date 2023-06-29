# 4179 불!  -  불 먼저 돌리고 지훈이 돌리니 메모리 초과 따라서 턴마다 task 처리
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

