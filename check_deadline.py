# Обработка дедлайнов
import datetime
from datetime import datetime, date, timedelta

#Запрос у пользователя данных
created_date = datetime.now()  # сегодняшняя дата
print(f'Дата создания заметки - {created_date.strftime('%d-%m-%Y')}')  # вывод сегодняшней даты
issue_date = input('Введите дату дедлайна в формате дд-мм-гггг: ')  #запрос у пользователя дату дедлайна

#цикл предназначеный для введения даты дедлайна в случае ошибки
while True:
    try: #используем конструкцию try для того, чтобы в случае не верного ввода программа продолжала работать.
        deadline = datetime.strptime(issue_date, '%d-%m-%Y')
        print(f'Дата дедлайна {deadline.strftime('%d-%m-%Y')}')
        time_delta = deadline - created_date
        time_delta = int(time_delta.days) + 1

#проверяем условия
        if time_delta == 0:
            print('Дедлайн сегодня!')
        elif time_delta > 0:
            print(f'Дней осталось до дедлайна: {time_delta}')
        elif time_delta < 0:
            print(f'{time_delta*-1}!!!Именно столько дней назад истек дедлайн!.')
        break

    except ValueError:
        print(f'Вы ввели не правильный формат даты попробуйте еще раз')
        issue_date = input('Введите дату дедлайна в формате дд-мм-гггг: ')

