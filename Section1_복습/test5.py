'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[:2])
print(msg[:1])
print(msg[3:5])
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

# isalpha는 공백이 아닌것에서 True.
for x in msg:
    if x.isalpha():
        print(x, end='')
print()

tmp = 'AZaz'
# ord()는 ASCII Number를 출력해줌.
for x in tmp:
    print(ord(x))

tmp = 65
# ASCII Number를 대응되는 문자로 출력
print(chr(tmp))
