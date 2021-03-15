'''
조건문 if(분기, 중첩)


x = 16
if x >= 10 :
    if x % 2 == 1:
        print("10이상의 홀수")
    elif x % 2 == 0:
        print("10이상의 정수")


x = 10
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")
    elif x >= 10:
        print("10보다 큰 자연수")


x = 7
if x > 0 and x < 10:
    print("10보다 작은 자연수")


x = 7
if 0 < x < 10:
    print("10보다 작은 자연수")


x = input("숫자를 입력하세요: ")
x = int(x)
if x > 0:
    print("양수")
elif x == 0:
    print("Zero")
else:
    print("음수")
'''

x = input("점수를 입력하세요: ")
x = int(x)
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
else:
    print('F')
    
