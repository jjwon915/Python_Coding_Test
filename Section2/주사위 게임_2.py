# 주사위 게임
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
max = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    
    if a == b and b == c:
        result = 10000 + a * 1000
    
    elif a == b or a == c:
        result = 1000 + a * 100

    elif b == c:
        result = 1000 + b * 100

    else:
        result = c * 100

    if result > max:
        max = result

print(max)