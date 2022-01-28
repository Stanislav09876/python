def convert_time(duration: int) -> str:
    if duration < 60:
        indicator = (duration, "сек")
    elif duration < 3600:
        indicator = (duration//60, 'мин', duration%60, 'сек')
    elif duration < 84600:
        indicator = (duration//3600, "час", duration%3600, 'мин', duration%3600%60, 'сек')
    else:
        indicator = (duration//84600, 'дня', duration%84600//3600, "час",  duration%84600%3600//60, 'мин', duration%84600%3600%60, 'сек')

    return(indicator)


duration = 400153
result = convert_time(duration)
print(result)