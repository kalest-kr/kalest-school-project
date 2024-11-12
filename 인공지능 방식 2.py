from algorithm_data_set import list1
import time

sorted_list = sorted(list1)

print(sorted_list)

searching_number = int(input('검색 값: '))

start_time = time.time()

count = 0
end = len(list1) - 1

while True:
    if searching_number != sorted_list[count]:
        count += 1
    if searching_number == sorted_list[count]:
        print(count + 1, '째 자리')
        break
else:
    print('찾는 값이 존재하지 않음')
end_time = time.time()
execution_time = end_time - start_time
print("실행 시간:", execution_time, "초")
