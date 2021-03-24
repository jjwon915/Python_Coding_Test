# 뮤직비디오(결정알고리즘)
import sys

#sys.stdin = open("input.txt", "rt")

def Count(capacity):
    cnt = 1
    sum = 0
    for x in a:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 음악들 중 가장 길이가 긴 것. 
largest = max(a)
lt = 1
rt = sum(a)
res = 0

while lt <= rt:
    mid = (lt+rt) // 2
    # mid는 가장 길이가 긴 음악보다는 길어야 한다.
    if mid >= largest and Count(mid) <= m:
        res = mid
        rt = mid - 1
    elif Count(mid) > m:
        lt = mid + 1

print(res)