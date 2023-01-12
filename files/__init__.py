import os.path

FILE_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILE_DIR, filename)


BOOKS_FILE_PATH = get_path(filename="books.csv")
RESULT_FILE_PATH = get_path(filename="result.json")
USERS_FILE_PATH = get_path(filename="users.json")
