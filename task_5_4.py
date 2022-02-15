def get_numbers(src: list):
    list_up = []
    for i in range(1, len(src)):
        if src[i] > src[i-1]:
            list_up.append(src[i])
    return list_up

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))