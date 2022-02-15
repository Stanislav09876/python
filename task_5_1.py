def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    pass
    for num_x2 in range(1, number + 1, 2):
        yield num_x2


n = 15
generator = odd_nums(n)
for _ in range(1, n+1, 2):
    print(next(generator))
#next(generator)


