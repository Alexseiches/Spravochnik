import re 

def find_by_lastname(Phonebook, searchString):
    for i in Phonebook:
        if i["Фамилия"] == searchString:
            return i
        
def find_by_phone(Phonebook, searchString):
    for i in Phonebook:
        if i["Телефон"] == searchString:
            return i

def add_user(data):
    write_txt(f'\n{data}')


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('Phonebook.txt')
    
    while (choice != 6):
        if choice == 1:
            print(phone_book)
        elif choice == 2:
            last_name = input('Lastname: ').strip()
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Phone number: ')
            print(find_by_phone(phone_book, number))
        elif choice == 4:
            print('Введите данные через запятую')
            text = input()
            add_user(text)
        elif choice == 5:
            number = input('number')
            print(find_by_number(phone_book.number))
        elif choice == 6:
            return
        
        choise = show_menu()

def read_txt (Phonebook):
    phone_book = []
    fileds = ['Фамилия',"Имя","Телефон"]
    

    with open(Phonebook,'r',encoding = 'utf-8') as phb:
        for line in phb:
            str = re.sub('\s+', '', line)
            record = dict(zip(fileds,str.split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(data):
    f = open('Phonebook.txt', 'a')
    f.write(data)

def show_menu():
    print('\n Выберите необходимое действие :\n'
          '1.Отобразить весь справочник\n'
          '2.Найти обонента по фамилии\n'
          '3.Найти обонента по номеру телефона\n'
          '4.Добавить абонента в справочник\n'
          '5.Сохранить справочник в текстовом формате\n'
          '6.Закончить работу\n')
    return int(input())

work_with_phonebook()
