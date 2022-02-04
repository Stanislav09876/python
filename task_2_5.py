my_list = [34.12, 67.70, 12.53, 94.12, 52.65, 22.22, 45.22, 67.15, 17.90, 124.67]

#Часть 1
def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    print(list_in)


sort_prices(my_list)
print(id(my_list))

#Часть 2
def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    return list_out


result = sort_price_adv(my_list)
print(result)

#Часть 3

def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    all_prices = sorted(list_in, reverse=True)
    list_out = all_prices[:5]
    return list_out


result_2 = check_five_max_elements(my_list)
print(result_2)

