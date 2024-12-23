#Цикл для добавления заголовков

#Запрос ввода заголовков
titles = []
title = input("Введите заголовок заметки или оставьте пустым для отмены: ")
titles.append(title)

#Заполняем список
while True:
    title = input("Введите заголовок новой заметки или оставьте пустым для отмены: ")
    if title == '' or title == 'стоп':
        break
    titles.append(title)
    continue

#Выводим список заметок
print('\nСписок ваших заметок:')
print('\n'.join(titles))