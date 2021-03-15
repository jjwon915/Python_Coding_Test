''' 함수 : 메인 스크립트 위쪽에 작성. '''

'''
def add(a, b):
    sum = a + b
    print(sum)

a, b = map(int, input().split())
add(a, b)


def add(a, b):
    c = a + b
    return c

a, b = 10, 20
print(add(a, b))



def cal(a, b):
    c = a + b
    d = a - b
    return c, d

a, b = 4, 5
# tuple형식으로 출력됨.
print(cal(a, b))
'''
# 소수 판별 함수
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]

# 소수면 YES, 소수가 아니면 NO 출력
for x in a:
    if isPrime(x) == False:
        print(x, "NO")
    else:
        print(x, "YES")
