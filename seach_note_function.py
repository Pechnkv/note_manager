#  Поиск заметок

# функция вывода списка словарей
def print_notes(note_titles):
    if not note_titles:
        print('Список заметок пуст\n')
    else:
        print('Список заметок:\n')
        while True:
            i = 1
            for elements in note_titles:
                print(f'\tЗаметка № {i}')
                i += 1
                for key, value in elements.items():
                    print("{0}: {1}".format(key, value))
                print('\n')
            break

# функция поиска совпадений в списке словарей/заметок
def search_notes(notes, keyword=None, status=None):
    # создаем новый список в который будем помещать совпадающие значения
    new_notes = []
    # создаем переменную, значение которой будет являтся счетчиком для выявления отсутствия совпадений
    result = 0
    # реализуем условие при котором заданы две переменные функции
    if keyword and status is not None:
        notes_for_some_params = []
        # для первой переменной функции циклом проходимся по словарям и ищем совпадения. Совпадающие ключ-значения передаем в новый список
        for note in notes:
            for value in note.values():
                if keyword.strip().lower() == value.lower().strip():
                    notes_for_some_params.append(note)
                    result += 1
                else:
                    continue
        # Далее в новом списке осуществляем поиск по второй переменной, переданной в функцию и все совпадения передаем в созданный для функции список
        for note_ in notes_for_some_params:
            for value_ in note_.values():
                if status.strip().lower() == value_.lower().strip():
                    new_notes.append(note_)
                    result += 1
                else:
                    continue
    # реализуем тот случай если передано только первое значение для поиска
    elif keyword is not None:
        for note in notes:
            for value in note.values():
                if keyword.strip().lower() == value.lower().strip():
                    new_notes.append(note)
                    result += 1
                else:
                    continue
    # реализуем тот случай если передано только второе значение для поиска
    elif status is not None:
        for note in notes:
            for value in note.values():
                if keyword.strip().lower() == value.lower().strip():
                    new_notes.append(note)
                    result += 1
                else:
                    continue
    # счетчик совпадений
    if result == 0:
        print(f'Заметок не найдено')
    # возвращаем список словарей
    return new_notes

# Пример для проверки работоспособности функций. Создаем список словарей
notes = [{'Имя пользователя': 'Андрей', 'Статус': 'Новая'},
         {'Имя пользователя': 'Маша', 'Статус': 'В работе'},
         {'Имя пользователя': 'Андрей', 'Статус': 'Активна'}]

# Заполняем переменные для проверки функции
keyword = 'Андрей'
status = 'Новая'
new_notes = []

# Заполняем список словарей используя функцию в которую передаем 2 значения
new_notes = print_notes(search_notes(notes, keyword, status))