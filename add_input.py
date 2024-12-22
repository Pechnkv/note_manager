#Запрашиваем у пользователя ввод данных
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате 11-11-2024: ")
issue_date = input("Введите дату редактирования формате 11-11-2024: ")
temp_issue_date = issue_date[:5]
temp_created_date = created_date[:5]

#Выводим данные
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)

