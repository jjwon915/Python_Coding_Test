# 주사위 게임
import sys

#sys.stdin = open("input.txt", "rt")

'''
규칙(1) : 같은 눈이 3개가 나오면 10000 + 같은눈*1000
규칙(2) : 같은 눈이 2개가 나오는 경우 1000 + 같은 눈 * 100
규칙(3) : 모두 다른 눈 : 가장 큰 눈 * 100
'''

n = int(input())
arr = []

for i in range(n):
    a = list(map(int, input().split()))
    same = a[0]
    cnt = 0
    for x in a:
        if x == same:
            cnt += 1
            same = x
    
    if cnt == 2:
        result = 1000 + same * 100
        arr.append(result)

    elif cnt == 3:
        result = 10000 + same * 1000
        arr.append(result)

    elif cnt == 1:
        a.sort()
        result = a[0] * 100
        arr.append(result)

arr.sort(reverse=True)
print(arr[0])