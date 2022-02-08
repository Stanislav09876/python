nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    while True:
        from random import choice
        a = choice(nouns)
        b = choice(adverbs)
        c = choice(adjectives)
        joke = [a, b, c]
        jokes = ' '.join(joke)
        list_out.append(jokes)
        if len(list_out) == count:
            break
    return list_out


print(get_jokes(2))
print(get_jokes(10))