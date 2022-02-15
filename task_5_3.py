import itertools

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    result = list(itertools.zip_longest(tutors,klasses, fillvalue=None))
    return result

generator = check_gen(tutors, klasses)
print(generator)