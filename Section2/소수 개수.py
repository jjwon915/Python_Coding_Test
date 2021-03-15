# 소수(에라토스테네스 체)
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
ch = [0]*(n+1)
cnt = 0

for i in range(2, n + 1):
    if(ch[i] == 0):
        cnt += 1
        # range(i, n + 1, i) : start, end, step(증가)
        for j in range(i, n + 1, i):
                ch[j] = 1

print(cnt)
