# Удаление заметок

#функция удаления словаря из списка. т.е удаления заметки
def delete_notes(list):
    seach_key = input("Введите имя пользователя или заголовок заметки для удаления: ")
    new_list = []
    result = 0
    for i in range(len(list)):
        while True:
            if seach_key not in list[i].values():
                new_list.append(list[i])
                break
            else:
                result+=1
                break
    if result>0:
        print(f'Найдено и удалено заметок с совпаденями: {result}\nОстались следующие заметки:')
    if result==0:
        print(f'Заметок с ключевцым словом "{seach_key}" не найдено')
    if not new_list:
        print('Удалены все заметки, список пуст')
    return new_list

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

#Пример для проверки работоспособности функций. Создаем список словарей
list = [{'Имя пользователя': 'Андрей', 'Заголовок': 'Дом'},
        {'Имя пользователя': 'Маша', 'Заголовок': 'Учеба'}]

#Вывод начального списка словарей через функцию
print_notes(list)

#Вывод измененного списка словарей
print_notes(delete_notes(list))


