
# 대표값
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

# 반올림 round함수 사용. 파이썬의 round함수는 round_half_even방식 사용. 따라서 avg = (sum(arr)/n) + 0.5를 한 후 int형으로 형변환해 소수점아래를 없앤다. 
# 합계 구하기 sum함수 사용.
avg = int((sum(arr)/n) + 0.5)
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