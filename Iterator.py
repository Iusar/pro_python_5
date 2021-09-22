import json
import Decorator_task_3 as par_dec

class Countries_iterator():
    # Инициализация
    def __init__(self, json_object):
        self.country_number = None
        self.json_object = json_object

    def __iter__(self):
        self.country_number = 0
        return self

    # Метод чтения файла
    def open_object(self):
        with open(self.json_object, "r", encoding="utf-8") as f:
            file_content = f.read()
            countries = json.loads(file_content)
        return countries

    # Вывод названия по индексу
    def read_object(self):
        return self.open_object()[self.country_number]['name']['common']

    def __next__(self):
        # Условие итерации
        if self.country_number == len(self.open_object()) - 1:
            raise StopIteration
        else:
            self.country_number += 1
            return self.read_object()




@par_dec.param_decorator('C:\\Test_folder\\1\\2\\3')
def iterator_function(HOST):
    my_dict = {}
    # Собственно сам итератор
    for country_name in Countries_iterator('countries.json'):
        # Запись результатов в словарь
        my_dict[country_name] = str(HOST + country_name.replace(" ", "_"))
    pass

# Запись текстового файла для задания 2
    with open('countries_links.txt', 'w', encoding="utf-8") as f:
        for row in my_dict.keys():
            f.write(f'{str(row)}\n')


if __name__ == '__main__':

    HOST = 'https://wikipedia.org/wiki/'
    iterator_function(HOST)