# 회문 문자열
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())

for i in range(n):
    # 문자열 받기
    s = input().upper()
    # 문자열을 모두 대문자화 시킴
    size = len(s)
        
    for j in range(size // 2):
        # 배열 -1번째는 마지막 값이 접근된다.
        if s[j] != s[-1 - j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))