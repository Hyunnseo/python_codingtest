#상하좌우

n = input()
d = list(input().split())

r = 1
c = 1

for i in range(len(d)):   #흔히 있는 x y 좌표와 반대라서 헷갈릴 가능성 큼
    if (r == 1 and d[i] == 'L') or (r == n and d[i] == 'R') or (c == 1 and d[i] == 'U') or (c == n and d[i] == 'D'):
        continue

    else:
        if d[i] == 'R':
            r += 1
            print(r)
        if d[i] == 'L':
            r -= 1
            print(r)
        if d[i] == 'U':
            c -= 1
            print(c)
        if d[i] == 'D':
            c += 1
            print(c)

print(c, r)

