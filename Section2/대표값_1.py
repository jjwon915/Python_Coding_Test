
# 대표값
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

# 반올림 round함수 사용. 합계 구하기 sum함수 사용.
avg = round(sum(arr) / n)
diff = float('inf')
min = 0
num = 0

for i in range(n):
    if diff == abs(avg - arr[i]):
        if arr[num-1] < arr[i]:
            min = arr[i]
            diff = abs(avg - arr[i])
            num = i + 1
    elif diff > abs(avg - arr[i]):
        min = arr[i]
        diff = abs(avg - arr[i])
        num = i + 1

print(avg, end = ' ')
print(num)