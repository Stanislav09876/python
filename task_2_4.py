def convert_name_extract(list_in: list) -> list:
    list_out = []
    for i in list_in:
        names = i.split()[-1]
        list_out.append(f"Привет, {names.capitalize()}")
    print(list_out)



my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
convert_name_extract(my_list)
