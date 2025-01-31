# создаем функцию вывода списка словарей
def display_notes(notes):
    if not notes:
        print('Список заметок пуст\n_________________________________________')
    else:
        print('Список заметок:\n_________________________________________')
        while True:
            i = 1
            for elements in notes:
                print(f'\tЗаметка № {i}')
                i+=1
                for key, value in elements.items():
                    print("{0}: {1}".format(key, value))
                print('_________________________________________\n')
            break

#Пример для проверки работоспособности функций. Создаем несколько словарей
note_1 = {'Имя пользователя': 'Макс',
        'Заголовок заметки': 'Дом',
        'Описание заметки': 'Описание',
        'Статус заметки': 'В разработке',
        'Дата создания заметки': '12-12-2024',
        'Дедлайн': '11-12-2024'}

note_2 = {'Имя пользователя': 'Андрей',
        'Заголовок заметки': 'Работа',
        'Описание заметки': 'Описание',
        'Статус заметки': 'Новая',
        'Дата создания заметки': '30-12-2024',
        'Дедлайн': '11-01-2025'}

# создаем список словарей
list = [note_1, note_2]

# выводим список словарей используя функцию

display_notes(list)
