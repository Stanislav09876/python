def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    numb = {
        'zero': "ноль",
        'one': "один",
        'two': "два",
        'three': "три",
        'four': "четыре",
        'five': "пять",
        'six': "шесть",
        'seven': "семь",
        'eight': "восемь",
        'nine': "девять",
        'ten': "десять"
    }
    str_out = (numb.get(value))
    print(str_out)


num_translate('one')
num_translate('eight')