#볼링공 고르기

n, m = map(int, input().split())

bowl = list(map(int, input().split()))

i = 0
result = 0

while i < len(bowl):
    for j in range(i+1, len(bowl)):
        if bowl[i] != bowl[j]:
            result += 1
        else:
            continue

    i += 1

print(result)