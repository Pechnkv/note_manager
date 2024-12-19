
print ("Введите имя пользователя:")
username = input()
print ("Введите заголовок заметки:")
title = input()
print ("Введите описание заметки:")
content = input()
print ("Введите статус заметки:")
status = input()
print ("Введите дату создания заметки:")
created_date = input()
#issue_date = input()
print ("Введите подзаголовки:")

print ("Введите подзаголовок №1:")
title_1 = input()
print ("Введите подзаголовок №2:")
title_2 = input()
print ("Введите подзаголовок №3:")
title_3 = input()

print ("Имя пользователя:", username)
print ("Заголовок заметки:", title)
print ("Описание заметки:", content)
print ("Статус заметки:", status)
print ("Дата создания заметки:", created_date)
#print ("Дата истечения заметки:", issue_date)

titles = [title_1, title_2,title_3]

note = [username,title,status,
created_date, titles
]

print(note)
