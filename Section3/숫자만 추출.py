# 숫자만 추출
import sys

#sys.stdin = open("input.txt", "rt")

n = input()
res = 0

for i in n:
    # isdecimal : 0~9까지 숫자인지 판별. 
    if i.isdecimal():
        res = res * 10 + int(i)

print(res)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1

print(cnt)