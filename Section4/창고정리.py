# 창고정리
import sys

#sys.stdin = open("input.txt", "rt")

l = int(input())

a = list(map(int, input().split()))

m = int(input())

for i in range(m):
    a.sort()
    a[0] = a[0] + 1
    a[l-1] = a[l-1] -1

a.sort()
print(a[l-1]-a[0])