print ("Введите дату создания заметки в формате 11-11-2024:")
created_date = input()
print ("Введите дату редактирования формате 11-11-2024:")
issue_date = input()

temp_issue_date = issue_date[6:]
temp_created_date = created_date[6:]

print("Дата создания заметки", temp_created_date)
print("Дата изменения заметки", temp_issue_date)


