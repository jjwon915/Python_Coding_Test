'''변수명
1) 영문과 숫자, _로 이루어진다.
2) 대소문자 구분
3) 문자나, _로 시작
4) 특수문자 불가능
5) 키워드를 사용하면 안됨(if, for등)
'''
a = 1
A = 2
A1 = 3
#_b = 4
print(a, A, A1)

# 한꺼번에 동시에 선언, 초기화 가능
a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a = 1234567896789678967896789
print(a, type(a))
a = 12.123456789123456789
print(a, type(a))
a = 'student'
print(a, type(a))

# 출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number", a, b, c)
# sep : 각 변수 사이 지정
print(a, b, c, sep = ' + ')
print(a, b, c, sep = '')
print(a, b, c, sep = '\n')
# print는 자동으로 \n을 하는데 이것을 없애려면 end 사용
print(a, end=' ')
print(b, end=' ')
print(c)

# 변수 입력과 연산자
'''
a = input("숫자를 입력하세요: ")
print(a)

#split함수는 띄어쓰기를 분리자로 받아들여 a, b에 값을 입력받는다.
a, b = input("숫자를 입력하세요 : ").split()
print(type(a))
c = a + b
print(type(c))
print(c)
# str형으로 받아들여서 연결되어서 출력됨.
print(a + b)
#int형으로 형변환 시켜줘야 함.
a = int(a)
b = int(b)
print(a+b)


#입력받아서 바로 int형으로 변환.
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)

'''

a = 4.3
b = 5
c = a + b
print(c, type(c))
