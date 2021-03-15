# 정다면체
import sys

#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

arr = [0]*(n+m+3)
max = -2147000000

# 합계 count list에 count한다.
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j] += 1

# 최대 count를 찾아서 max에 저장
for i in range(n+m+1):
    if arr[i]> max:
        max = i

# 찾은 count와 같은 값을 가지는 list의 index값 출력.
for i in range(n+m+1):
    if arr[i] == max:
        print(i, end=' ')

print()