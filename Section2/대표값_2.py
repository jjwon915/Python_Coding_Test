
# 대표값
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

# 반올림 round함수 사용. 합계 구하기 sum함수 사용.
avg = round(sum(arr) / n)
min = 2147000000

# enumerate : list의 index값과 value값을 쌍으로 대응해줌.
for index, x in enumerate(arr):
    tmp = abs(x - avg)
    if tmp < min :
        min = tmp
        score = x
        res = index + 1
    elif tmp == min:
        if x > score:
            score = x
            res = index + 1

print(avg, res)