def transform_string(number: int) -> str:
    if number == 1 or number%10==1:
        percent = (number, 'процент')
    elif number == 2 or number == 3 or number == 4 or number%10==2 or number%10==3 or number%10==4:
        percent = (number, 'процента')
    else:
        percent = (number, 'процентов')
    return percent

for n in range(1, 101):
    print(transform_string(n))