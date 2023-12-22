import json
import sys

# Чтение данных из файлов
with open(sys.argv[1], 'r') as tests_file:
    tests_data = json.load(tests_file)

with open(sys.argv[2], 'r') as values_file:
    values_data = json.load(values_file)

# Функция для заполнения значений в структуре tests_data на основе значений из values_data
def fill_values(tests, values):
    # Проверка, является ли текущий элемент словарем
    if isinstance(tests, dict):
        # Перебор ключей в словаре
        for key in tests.keys():
            # Если ключ существует в values_data, заполнение значения
            if key in values:
                tests[key]['value'] = values[key]
            # Рекурсивный вызов функции для вложенных структур
            fill_values(tests[key], values)
    # Проверка, является ли текущий элемент списком
    elif isinstance(tests, list):
        # Перебор элементов списка
        for item in tests:
            # Рекурсивный вызов функции для вложенных структур
            fill_values(item, values)

# Заполнение значений в структуре tests_data
fill_values(tests_data, values_data)

# Запись структуры tests_data с заполненными значениями в файл report.json
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)