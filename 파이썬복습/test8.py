'''2차원 리스트'''
# 0값을 10개 가지는 크기가 10인 리스트 a 생성.
#a = [0]*10
#print(a)

# for _ 는 변수 없이 실행. 2차원 리스트 생성.
a = [[0]*3 for _ in range(3)]
print(a)
a[0][1] = 1
a[1][1] = 2
print(a)
print()

# 2차원 리스트를 표 형태로 출력
for x in a:
    print(x)

# 괄호 없이 값만 표 형태로 출력 
for x in a:
    for y in x:
        print(y, end=' ')
    print()
