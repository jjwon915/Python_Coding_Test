# 뒤집은 소수
import sys

#sys.stdin = open("input.txt", "rt")

def reverse(x):
    result = 0
    while x > 0:
        result = result * 10 + x % 10
        x = x // 10
    return result

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

n = int(input())

a = list(map(int, input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp) == True:
        print(tmp, end = ' ')