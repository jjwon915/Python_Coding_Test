# 점수 계산
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
sum = 0

for i in arr:
    if i == 1:
        cnt += 1
        sum += cnt
    elif i == 0:
        cnt = 0

print(sum)
