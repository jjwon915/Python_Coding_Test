# 카드 역배치
import sys

#sys.stdin = open("input.txt", "rt")

# 0 부터 20까지 list 생성.
a = list(range(21))

# _를 쓰면 변수 없이 반복.
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)

for i in a:
    print(i, end =' ')