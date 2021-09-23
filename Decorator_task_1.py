import os, hashlib
from datetime import datetime


def decorator(foo):
    def wrap(*args, **kwargs):

        result = foo(*args, **kwargs)

        time = datetime.now().time()
        date = datetime.now().date()

        with open('log_file.txt', 'a') as log:
            log.write(
                f'дата - {date}, время - {time}, функция - {foo.__name__}, результат {result}, args - {args}, kwargs - {kwargs})\n')
        return result
    return wrap


@decorator
def create_list(value, size):
    return [value] * size


if __name__ == '__main__':
    print(create_list('2', 5))
