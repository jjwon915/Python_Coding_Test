'''
리스트와 내장함수(2)
'''

a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

# enumerate()는 index번호와 함께 (index, 값) 이런 tuple 형식으로 출력된다.
for x in enumerate(a):
    print(x)
    
# () 소괄호로 열면 tuple, list와의 차이점은 값을 변경할 수 없다.
b = (1, 2, 3, 4, 5)
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

# 60 > x인 것이 모든 값에서 참이면 True를 return한다. 하나라도 맞지 않으면 False를 return
if all(50 > x for x in a):
    print("YES")
else:
    print("NO")

# any는 한개만 참이여도 True를 return한다. 모두 거짓인 경우에만 False return
if any(15 > x for x in a):
    print("YES")
else:
    print("NO")

    
