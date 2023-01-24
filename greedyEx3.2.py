#숫자 카드 게임

n,m = map(int, input().split())

min_value = 0
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    #result에 바로 result와 min을 비교한 값을 넣는다
    result = max(result, min_value)

print(result)


