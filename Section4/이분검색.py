# 이분검색
import sys

#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 이분검색을 하기 위해서는 먼저 정렬이 되어있어야 한다. 
a.sort()

lt = 0
rt = n-1
mid = (lt + rt) // 2

while lt <= rt:
    if a[mid] > m:
        rt = mid -1
        mid = (lt + rt) // 2
    elif a[mid] < m:
        lt = mid + 1
        mid = (lt + rt) //2
    elif a[mid] == m:
        break

print(mid + 1)
