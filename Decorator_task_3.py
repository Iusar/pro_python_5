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

        return wrap

    return decorator


