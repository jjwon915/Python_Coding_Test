# 회문 문자열
import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

for i in range(n):
    # 문자열 받기, 문자열을 모두 대문자화 시킴
    s = input().upper()
    
    # s를 거꾸로 reverse해서 비교.
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
    