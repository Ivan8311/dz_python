# Задача №49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной



# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.



book = 'phone.txt'
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_text(book)

    while choice != 7:

        if choice == 1:
            print_result(phone_book)
            
        elif choice == 2:
            print('Напишите фамилию: ')
            last = input()
            print_result(find_by_lastname(phone_book, last))
        
        elif choice == 3:
            phone = input('напишите номер телефона: ')
            print_result(find_by_number(phone_book, phone))

        elif choice == 4:
            last = input('Напишите фамилию, чьи данные хотите удалить: ')
            result = delete_by_lastname(phone_book, last)
            print(result)
            write_text(book, phone_book)

        elif choice == 5:
            last = input('Напишите фамилию, чей номер хотите изменить: ')
            nam = input('Напишите имя, чей номер хотите изменить: ')
            new_number = input('Введите новый номер телефона: ')
            result = to_change_number(phone_book, nam, last, new_number)
            print(result)
            write_text(book, phone_book)

        elif choice == 6:
            user = input('Введите данные нового абонента(фамилия, имя, телефон, описание:)')
            add_user(phone_book, user)
            write_text(book, phone_book)
            print('добавлен новый абонент')

   

        choice = show_menu()

def show_menu(): 
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Удалить абонента по фамилии\n"
          "5. Изменить номер абонента\n"
          "6. Добавить абонента в справочник\n"
          "7. Закончить работу")

    choice = int(input("Введите номер: "))
    return choice

# функция создает словари с ключами, где ключи это atribute и сохранияет в список phone_book.
def read_text(filename):
    phone_book = []
    atribute = ['lastname', 'name', 'phoneNumber', 'description']
    with open(book, 'r', encoding="utf-8") as dic:
        for line in dic:
            diction = dict(zip(atribute, line.strip().split(",")))
            phone_book.append(diction)
        return phone_book

# функция для перезаписывания файла
def write_text(filename, phone_book):
    with open(filename, 'w',encoding='utf-8') as new_phone_book:
        for line in phone_book:
            new_phone_book.write(','.join(line.values()) + '\n')

# функция печатает построчно по вызовам
def print_result(phone_book):
    for line in phone_book:
        print(line)


def find_by_lastname(phone_book, last):
    return[line for line in phone_book if line['lastname'] == last]

def find_by_number(phone_book, phone):
    return[line for line in phone_book if line['phoneNumber'].strip() == phone]

def delete_by_lastname(phone_book, last):
    for line in phone_book:
        if line['lastname'].strip() == last:
            phone_book.remove(line)
            return(f"Данные абонента {last} удаленны")
    return("абонент с данной фамилией не найден")

def to_change_number(phone_book, nam, last, new_number):
    for line in phone_book:
        if line['lastname'].strip() == last and line['name'].strip() == nam:           
            line['phoneNumber'] = new_number
            return('номер был изменен')
    return("абонент с данной фамилией и именем не найден")

def add_user(phone_book, user):
        atribute = ['lastname', 'name', 'phoneNumber', 'description']
        new_user = dict(zip(atribute, user.strip().split(",")))
        phone_book.append(new_user)

work_with_phonebook()