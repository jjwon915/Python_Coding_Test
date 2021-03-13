''' 람다함수(=익명의 함수) '''

# 일반 함수
def plus_one(x):
    return x+1

print(plus_one(1))


plus_two = lambda x : x+2
print(plus_two(1))

# 람다함수는 내장함수의 인자로 사용될 때 편리.

a = [1, 2, 3]
print(list(map(plus_one, a)))

a = [1, 2, 3]
print(list(map(lambda x: x+1, a)))
