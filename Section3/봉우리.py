# 봉우리
import sys

#sys.stdin = open("input.txt", "rt")

# 봉우리인지 확인하기 위한 좌표 리스트. 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 0번 행에 n개 0 삽입.
a.insert(0, [0]*n)
# 맨 마지막 행에 0으로 된 행 삽입.
a.append([0]*n)

for x in a:
    # 각 행 맨 앞에 0 삽입.
    x.insert(0, 0)
    # 각 행의 맨 뒤에 0 삽입.
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)