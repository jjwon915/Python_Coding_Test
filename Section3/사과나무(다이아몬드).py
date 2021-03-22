# 사과나무(다이아몬드)
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())

# 한 줄을 읽어서 list화 하는 것을 n번 실행.
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n //2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)