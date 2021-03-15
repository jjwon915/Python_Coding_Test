'''
반복문(for, while)

# range는 순차적으로 정수 list를 만드는 함수
a = range(1, 11)
print(list(a))


for i in range(1, 10):
    print(i)

#1씩 감소하게 하려면 -1을 추가해야한다. 
for i in range(10, 0, -3):
    print(i)

#1부터 10까지 while문을 통해 출력
i = 1
while i <= 10:
    print(i)
    i = i+1

i = 10
while i > 0:
    print(i)
    i = i-1

i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1

for i  in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
'''

for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:
    print(11)
    
