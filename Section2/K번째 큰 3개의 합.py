
# k번째 큰 수
import sys

#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

a = list(map(int, input().split()))

# 중복제거 : set()
res = set()

# 숫자 3개를 뽑아 sum. 
for i in range(n): 
    for j in range(i+1, n):
        for m in range(j+1, n):
            # res에 중복은 제거되면서 추가됨.
            res.add(a[i] + a[j] + a[m])

# set은 sort()가 불가능 하므로 list로 형변환
res = list(res)
res.sort(reverse = True)
print(res[k-1])