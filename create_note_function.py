#Создание новой заметки и возврат словаря


note = {}

get_user()



def get_user(note):

    note_1 = {}

    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки: ")
    created_date = input("Введите дату создания заметки в формате '11-11-2024': ")
    issue_date = input("Введите дату истечения заметки в формате '11-11-2024': ")

    note = {"Имя пользователя: ": username,
            "Описание заметки: ": content,
            "Статус заметки: ": status,
            "Дата создания заметки: ": temp_created_date,
            "Дата истечения заметки: ": temp_issue_date,
            "Заголовки: ": titles}





    return note
