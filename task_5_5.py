def get_uniq_numbers(src: list):
    result_list = []
    for i in src:
        if src.count(i) == 1:
            result_list.append(i)
    return result_list


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))