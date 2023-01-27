#문자열 뒤집기
import time
start_time = time.time()   #측정 시작

number = input()
num_list = list(number)
n = list(map(int, num_list))
print(n)

result = 0

if n[0] == n[len(n)-1] :   #양 끝이 같으면 첫번째 숫자랑 다른 그 숫자 개수.. 세면 됨
    k = n[0]
    for i in range(1,len(n)):
        if n[i] == k :
            continue
        else:
            result += 1
            k = n[i]
    print(result//2)


else:   #양끝이 다르면 아무거나 뒤집으면 됨
    k = n[0]
    for i in range(1, len(n)):
        if n[i] == k:
            continue
        else:
            result += 1
            k = n[i]
    print(result//2+1)

end_time = time.time()
print("timr :", end_time - start_time)  #수행 시간 출력