# Работа с несколькими заметками
import datetime
from datetime import datetime, date, timedelta

#функция проверки даты
def check_date():
    while True:
        try:  # используем конструкцию try для того, чтобы в случае не верного ввода программа продолжала работать.
            return ((datetime.strptime(input(), '%d-%m-%Y')).strftime('%d-%m-%Y')) #возвращаем строковое значения даты в формате дд-мм-ггг
            break
        except ValueError:
            print(f'Вы ввели не правильный формат даты попробуйте еще раз в формате дд-мм-гггг: ')

#функция ввода данных от пользователя
def user_input():
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки: ")
    print('Введите дату создания заметки')
    created_date = check_date()
    print('Введите дату дедлайна')
    issue_date = check_date()


    note = {"Имя пользователя ": username,
            "Заголовок заметки ": title,
            "Описание заметки ": content,
            "Статус заметки ": status,
            "Дата создания заметки ": created_date,
            "Дедлайн ": issue_date}


    return note #возвращаем заполненный словарь

#функция вывода заполненного списка
def print_notes(note_titles):
    if not note_titles:
        print('Список заметок пуст\n')
    else:
        print('Список заметок:\n')
        while True:
            i = 1
            for elements in note_titles:
                print(f'\tЗаметка № {i}')
                i+=1
                for key, value in elements.items():
                    print("{0}: {1}".format(key, value))
                print('\n')
            break


#Начало работы программы
note_titles = []
change = input('Добро пожаловать в Менеджер заметок, хотите ли вы добавить новую заметку? (да/нет): ')

if change == 'да' or change == 'Да':
    user = user_input()
    note_titles.append(user)
    while True:
        new = input('Хотите ли вы добавить еще одну заметку? (да/нет): ')
        if new == 'да' or new == 'Да':
            user = user_input()
            note_titles.append(user)
        else:
            break

else:
    print('Жаль, что у вас нет идей для заметки')

#вывод
print_notes(note_titles)







