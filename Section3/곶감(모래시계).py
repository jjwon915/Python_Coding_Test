# 곶감(모래시계)
import sys

#sys.stdin = open("input.txt", "rt")

# 격자판
n = int(input())
# 한 줄을 읽어서 list화 하는 것을 n번 실행. 2차원 리스트로 받아옴.
a = [list(map(int, input().split())) for _ in range(n)]

# 회전 명령
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            # 맨 앞 값을 빼서 append. 
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            # 맨 뒤 값을 빼서(인덱스 없이 그냥 pop()) 맨 앞에 insert. 
            a[h-1].insert(0, a[h-1].pop())

s = 0
e = n-1
res = 0

for i in range(0, n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
