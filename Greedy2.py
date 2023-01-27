#곱하기 혹은 더하기
import time
start_time = time.time()   #측정 시작

number = input()
num_list = list(number)
int_list = list(map(int, num_list))
print(int_list)

if int_list[0] == 0 or int_list[0] == 1 or int_list[1] == 0 or int_list[1] == 1:
    result = int_list[0] + int_list[1]
else:
    result = int_list[0] * int_list[1]

for i in range(2, len(int_list)):
    if int_list[i] == 0 or int_list[i] == 1:
        result += int_list[i]
    else:
        result *= int_list[i]

print(result)

end_time = time.time()
print("timr :", end_time - start_time)  #수행 시간 출력