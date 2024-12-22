created_date = input("Введите дату создания заметки в формате 11-11-2024: ")
issue_date = input("Введите дату редактирования формате 11-11-2024: ")
temp_issue_date = issue_date[:5]
temp_created_date = created_date[:5]
print("Дата создания заметки", temp_created_date)
print("Дата изменения заметки", temp_issue_date)


