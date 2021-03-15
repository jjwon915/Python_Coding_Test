# 최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]

# arrMin = 가장 큰 값으로 초기화
arrMin = float('inf')

for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]

print(arrMin)
