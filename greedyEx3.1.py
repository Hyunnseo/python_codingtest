#배열 중에 가장 큰 수와 두번째로 큰 수만 필요함
#파이썬 map 내장함수 사용하여 입력받기

#n,m,k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

#data 무작위로 입력받기
data = list(map(int, input().split()))

#data 정렬해서 가장 큰 수, 두번째로 큰 수 찾기
data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)