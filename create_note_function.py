#Создание новой заметки и возврат словаря
import datetime
from datetime import datetime, date, timedelta

#функция запроса у пользователя данных для заполнения словаря.
def create_note():
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки: ")
    created_date = date.today().strftime('%d-%m-%Y')
    print('Введите дату дедлайна')
    issue_date = check_date()

    note = {"Имя пользователя ": username,
            "Заголовок заметки ": title,
            "Описание заметки ": content,
            "Статус заметки ": status,
            "Дата создания заметки ": created_date,
            "Дедлайн ": issue_date}

    return note

# функция проверки введенной даты на правильность
def check_date ():
    while True:
        try:  # используем конструкцию try для того, чтобы в случае не верного ввода программа продолжала работать.
            data = (datetime.strptime(input(), '%d-%m-%Y')).strftime('%d-%m-%Y')
            return data
            break
        except ValueError:
            print(f'Вы ввели не правильный формат даты попробуйте еще раз в формате дд-мм-гггг: ')

# функция вывода словаря
def print_note(note):
    print('\nСоздана новая заметка')
    for key, value in note.items():
        print("{0}: {1}".format(key, value))
    print('\n')

#создаем словарь и заполняем его используя функцию
note = create_note()

# функцией выводим словарь
print_note(note)

