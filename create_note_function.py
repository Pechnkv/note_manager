#Создание новой заметки и возврат словаря
import datetime
from datetime import datetime, date, timedelta


def user_input():
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки: ")
    print('Введите дату создания заметки')
    created_date = check_date()
    print('Введите дату дедлайна')
    issue_date = check_date()

    titles = []

    note = {"Имя пользователя: ": username,
            "Заголовок заметки: ": title,
            "Описание заметки: ": content,
            "Статус заметки: ": status,
            "Дата создания заметки: ": created_date,
            "Дедлайн: ": issue_date,
            "Заголовки: ": titles}

    return note

def check_date ():
    while True:
        try:  # используем конструкцию try для того, чтобы в случае не верного ввода программа продолжала работать.
            data = datetime.strptime(input(), '%d-%m-%Y')
            return data
            break
        except ValueError:
            print(f'Вы ввели не правильный формат даты попробуйте еще раз в формате дд-мм-гггг: ')