def thesaurus(*args) -> dict:
    dict_out = {}
    for value in sorted(args):
        key = value[0]
        dict_out.setdefault(key, []).append(value)
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))