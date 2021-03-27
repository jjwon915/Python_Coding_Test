# 회의실 배정(그리디)
import sys

#sys.stdin = open("input.txt", "rt")

n = int(input())

meeting = []

for i in range(n):
    s, e = map(int, input().split())
    # list에 tuple 형태로 append
    meeting.append((s,e))
    
# x[1]이 우선순위로 정렬, x[0]이 차순
meeting.sort(key=lambda x : (x[1], x[0]))

et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)