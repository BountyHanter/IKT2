import json
import os
from name_file import name as filename
from is_numbers import is_number as is_not_number


def add_data(new_dict):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    data.append(new_dict)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def take_info():
    name = input('Введите имя\n')
    surname = input('Введите фамилию\n')
    while True:
        gg = input('Ведите год рождения\n')
        if is_not_number(gg):
            age = gg
            break
        else:
            print('Вы ввели год не корректно, повторите')
    num_dict = {1: "Среднее", 2: "Высшее", 3: "Кандидат наук", 4: "Доктор наук"}
    print("Введите образование, посредство ввода цифры")
    while True:
        try:
            num = int(input("1: Среднее\n2:Высшее\n3: Кандидат наук\n4: Доктор наук\n"))
            if num not in num_dict:
                raise ValueError
            break
        except ValueError:
            print("Введено неверное число. Пожалуйста, попробуйте еще раз.")

    education = num_dict.get(num)

    final_dict ={'name': name, 'surname':surname, 'age': age, 'education': education}
    add_data(final_dict)


def find_info():
    surname = input('Введите фамилию для поиска:\n')
    result = None
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for person in data:
            if person['surname'] == surname:
                result = person
                break
    if result is None:
        print("Фамилия не найдена.\n")
    else:
        print(f'Имя: {result["name"]}\nФамилия: {result["surname"]},\nГод рождения: {result["age"]},\nОбразование: {result["education"]}\n')


def correct_info():
    surname = input('Введите фамилию для поиска:\n')
    result = None
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for person in data:
            if person['surname'] == surname:
                result = person
                break
    if result is None:
        print("Фамилия не найдена.")
    else:
        while True:
            print(f'Что вы хотите изменить?\n1: Имя\n2: Фамилия\n3: Год рождения\n4: Образование\n0: Завершить')
            choice = (input())
            if choice == '1':
                result['name'] = input("Введите новое имя:\n")
            elif choice == '2':
                result['surname'] = input("Введите новую фамилию:\n")
            elif choice == '3':
                while True:
                    gg = input('Ведите новый год рождения\n')
                    if is_not_number(gg):
                        age = gg
                        break
                    else:
                        print('Вы ввели год не корректно, повторите')
            elif choice == '4':
                print("Введите новое образование:")
                num_dict = {1: "Среднее", 2: "Высшее", 3: "Кандидат наук", 4: "Доктор наук"}
                while True:
                    try:
                        num = int(input("1: Среднее\n2:Высшее\n3: Кандидат наук\n4: Доктор наук\n"))
                        if num not in num_dict:
                            raise ValueError
                        break
                    except ValueError:
                        print("Введено неверное число. Пожалуйста, попробуйте еще раз.")
                result['education'] = num_dict.get(num)
            elif choice == '0':
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def take_json():
    def take():
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                # Попытка чтения и декодирования JSON
                data = json.load(f)
        except FileNotFoundError:
            print("Файл не найден.")
            return None  # или обработка ошибки
        except json.decoder.JSONDecodeError:
            print("Файл пуст или содержит некорректный JSON.")
            return None  # или обработка ошибки

        return data

    def print_json(data):
        if data is not None:
            print(json.dumps(data, indent=4, ensure_ascii=False))

    data = take()
    print_json(data)


def print_all_info():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Попытка чтения и декодирования JSON
            data = json.load(f)
    except FileNotFoundError:
        print("Файл не найден.")
        return None  # или обработка ошибки
    except json.decoder.JSONDecodeError:
        print("Файл пуст или содержит некорректный JSON.")
        return None  # или обработка ошибки
    for person in data:
        print(f"Имя: {person['name']}, Фамилия: {person['surname']}, Год рождения: {person['age']}, Образование: {person['education']}")
    print('\n\n')


def start():
    print('Привет, что будем делать?')
    while True:
        choice = (input(
                           '0 - Выход\n'
                           '1 - Добавить информацию\n'
                           '2 - Редактировать информацию\n'
                           '3 - Найти информацию\n'
                           '4 - Вывести информацию\n'
                           '5 - Вывести сырую информацию\n'
        ))
        if choice == '0':
            print('Всего доброго')
            break
        elif choice == '1':
            take_info()
        elif choice == '2':
            correct_info()
        elif choice == '3':
            find_info()
        elif choice == '4':
            print_all_info()
        elif choice == '5':
            take_json()
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == '__main__':
    start()
    
