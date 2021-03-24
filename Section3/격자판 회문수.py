# 격자판 회문수
import sys

#sys.stdin = open("input.txt", "rt")

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# i가 0-4, 1-5, 2-6 이런식으로 5개씩 확인.
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5] # slice 기능. (5개씩 분리) : 행 탐색
        if tmp == tmp[::-1]: # 역순
            cnt += 1
        for k in range(2): # 열탐색 : 2번만 하면 된다. 
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)