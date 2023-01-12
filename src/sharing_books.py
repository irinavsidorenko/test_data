from files import USERS_FILE_PATH, BOOKS_FILE_PATH, RESULT_FILE_PATH
import json
from csv import DictReader


books_dict_template = {'Title': None, 'Author': None, 'Pages': None, 'Genre': None}
users_dict_template = {'name': None, 'gender': None, 'address': None, 'age': None, 'books': []}

"""Create books dictionary by template"""


def generate_books(books_dict):
    for i in books_dict:
        for key, value in i.items():
            if 'Title' in key or 'Author' in key or 'Pages' in key or 'Genre' in key:
                books_dict_template[key] = value
        yield books_dict_template


"""Create users dictionary by template"""


def generate_users(users_dict):
    for i in users_dict:
        for key, value in i.items():
            if 'name' in key or 'gender' in key or 'address' in key or 'age' in key:
                users_dict_template[key] = value
        yield users_dict_template


with open(USERS_FILE_PATH, 'r') as users, open(BOOKS_FILE_PATH, 'r') as books, open(RESULT_FILE_PATH, 'w') as shared:
    json_reader = json.loads(users.read())  # считываем json построчно
    users_list = []  # словарь пользователей для цикла на раздачу книг
    for i in generate_users(json_reader):  # записываем данные в словарь по нужному шаблону
        users_list.append(users_dict_template.copy())

    csv_reader = DictReader(books)
    books_list = []  # словарь книг для цикла на раздачу книг
    for j in generate_books(csv_reader):  # записываем данные в словарь по нужному шаблону
        books_list.append(books_dict_template.copy())

    """Give books to users"""

    user_counter = -1
    for book_counter in range(len(books_list)):
        if user_counter == len(users_list) - 1:
            user_counter = 0
        else:
            user_counter = user_counter + 1
        users_list[user_counter]['books'] = users_list[user_counter]['books'] + [books_list[book_counter]]
    json.dump(users_list, shared, indent=4)
