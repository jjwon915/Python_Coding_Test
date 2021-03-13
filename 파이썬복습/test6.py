'''
리스트와 내장함수(1)
'''

import random as r

a = []
b = list() # ==> a와 b 모두 빈 리스트

a = [1, 2, 3, 4, 5]
#print(a[0])

b = list(range(1, 11))
#print(b)

c = a + b
#print(c)

print(a)
a.append(6)
print(a)

# insert : 3번 인덱스에 7을 넣음.
a.insert(3, 7)
print(a)

# 인자없는 pop : 맨 마지막 자리의 값이 사라짐.
a.pop()
print(a)
# 3인덱스의 값 사라짐.
a.pop(3)
print(a)

# 값을 찾아서 제거 : remove
a.remove(4)
print(a)

# 값을 찾아서 인덱스 번호를 return
print(a.index(5))

a = list(range(1, 11))
print(a)

# a리스트의 총합 : sum(a)
print(sum(a))

print(max(a))
print(min(a))
# 아래처럼 쓰면 인자들 중 최소값을 찾아 출력.
print(min(7, 5, 3))

# 무작위로 섞음 : random 모듈의 shuffle함수 사용.
print(a)
r.shuffle(a)
print(a)

#오름차순 정렬
a.sort()
print(a)

r.shuffle(a)
print(a)

# 내림차순 정렬 sort(reverse=True)
a.sort(reverse=True)
print(a)

# 빈 리스트 : clear()
a.clear()
print(a)
