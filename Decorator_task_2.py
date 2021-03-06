import os, hashlib
from datetime import datetime


def param_decorator(target_directory):
    def decorator(foo):
        def wrap(*args, **kwargs):

            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            result = foo(*args, **kwargs)

            time = datetime.now().time()
            date = datetime.now().date()


            with open(target_directory + '\\log_file.txt', 'a') as log:
                log.write(
                    f'дата - {date}, время - {time}, функция - {foo.__name__}, результат {result}, args - {args}, kwargs - {kwargs})\n')

            return result
        return wrap

    return decorator


@param_decorator('C:\\Test_folder\\1\\2\\3')
def create_list(value, size):
    return [value] * size


if __name__ == '__main__':
    print(create_list('2', 5))
