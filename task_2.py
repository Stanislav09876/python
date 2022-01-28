def sum_list_1(detaset: list) -> int:
    sum_division_1 = 0
    for i in range(len(detaset)):
        sum_div = 0
        number = detaset[i]
        while number != 0:
            sum_div += number%10
            number = number//10
        if sum_div%7 == 0:
            sum_division_1 = + detaset[i]
    return sum_division_1

def sum_list_2(detaset: list) -> int:
    sum_division_2 = 0
    for i in range(len(detaset)):
        detaset[i] += 17
    for i in range(len(detaset)):
        sum_div = 0
        number = detaset[i]
        while number != 0:
            sum_div += number%10
            number = number//10
        if sum_div%7==0:
            sum_division_2=+detaset[i]
    return sum_division_2

my_list = []
for cube in range(1, 1000, 2):
    my_list.append(cube**3)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)