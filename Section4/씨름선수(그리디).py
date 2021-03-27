# 씨름 선수(그리디)
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
info = []

for i in range(n):
    h, w = map(int, input().split())
    info.append((h, w))

info.sort(reverse = True)

largest = 0
cnt = 0

for s in info:
    if largest < s[1]:
        cnt += 1
        largest = s[1]

print(cnt)