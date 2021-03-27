# 침몰하는 타이타닉(그리디)
import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
w = deque(w)

cnt = 0

# w가 비어있으면 거짓이 되어서 멈춘다.
while w:
    # 마지막 한 명.
    if len(w) == 1: 
        cnt += 1
        break
    if (w[0] + w[-1]) > m:
        w.pop()
        cnt += 1
    else:
        w.popleft()
        w.pop()
        cnt += 1

print(cnt)