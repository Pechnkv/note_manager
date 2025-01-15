import datetime
from datetime import datetime, date, timedelta

# функция проверки даты
def check_date(text):
    print(text)
    while True:
        try:  # используем конструкцию try для того, чтобы в случае не верного ввода программа продолжала работать.
            data = (datetime.strptime(input(), '%d-%m-%Y')).strftime('%d-%m-%Y')
            return data
            break
        except ValueError:
            print(f'Вы ввели не правильный формат даты попробуйте еще раз в формате дд-мм-гггг: ')

# функция вывода полей словаря с возможностью изменения значения выбранного поля
def update_note(note):
    print('\nПоля заметок которые можно обновить:\n')
    for key, value in note.items():
        if key == 'Дата создания заметки':
            continue
        else:
            print("{0}".format(key))
    print('\n')
    while True:
        rewrite_key = input("Введите поле которое хотите обновить: ")
        if rewrite_key.strip().lower() not in note.__str__().lower():
            print('Вы ввели не верное имя поля, попробуйте еще раз')
            continue
        break
    for key, value in note.items():
        if rewrite_key.strip().lower() == key.strip().lower():
            rewrite_value = check_date(f"Введите новое значение для поля {key} : ")
            # rewrite_value = input(f"Введите новое значение для поля {key} : ").strip()
            new_note = {key: rewrite_value}
            note.update(new_note)
            break
        if rewrite_key.strip().lower() == key.strip().lower():
            rewrite_value = input(f"Введите новое значение для поля {key} : ").strip()
            new_note = {key: rewrite_value}
            note.update(new_note)
            break
    return note


created_date = date.today().strftime('%d-%m-%Y')

note = {'Имя пользователя': 'Макс',
        'Заголовок заметки': 'Дом',
        'Описание заметки': 'Описание',
        'Статус заметки': 'В разработке',
        'Дата создания заметки': created_date,
        'Дедлайн': '11-11-2024'}


note = update_note(note)



for key, value in note.items():
    print("{0}: {1}".format(key, value))
print('\n')


