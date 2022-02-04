def convert_list_in_str(list_in: list) -> list:
    for n, i in enumerate(new_list):
        if i.isdigit():
            new_list[n] = f"'{i.zliff(2)}'"
        elif i[1:].isdigit():
            new_list[n] = f"'{i[0]}{i[1:].zliff(2)}'"
    print(' '.join(new_list))


new_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
convert_list_in_str(new_list)



