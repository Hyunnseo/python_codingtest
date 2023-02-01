#시각
# 분, 초에 3이 들어가는 횟수를 일일이 다 셌을 때
n = int(input())

ms = 15 * 60 * 2 - 15*15
result = 0

#시에 3이 들어갈 때와 아닐 때 케이스를 나누어야 함
#3, 13, 23시 일때는 횟수 3600회이고 나머지의 경우는 계산하면 1575회

if n < 3:
    result = ms * (n + 1)

if n >= 3 & n < 13:
    result = ms * n + 60*60

if n >= 13 & n < 23:
    result = ms * (n-1) + 60 * 60 *2

if n == 23:
    result = ms * (n-2) + 60 * 60 * 3

print(result)