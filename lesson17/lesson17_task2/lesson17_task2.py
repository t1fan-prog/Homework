import unittest
import json

try:
    filename = 'phonebook.json'
    with open(filename) as f:
        file_dict = json.load(f)
except FileNotFoundError:
    print("There is no such a file in current directory")


def formatting(file_dict_local, a):
    """Функция добавляет или заменяет полученную информацию от юзера к данным, полученным из файла
    Если параметр 'a' - None, то функция добавляет, если же есть значение - заменяет"""
    first_name = input("Enter first name:\n")
    last_name = input("Enter last name:\n")
    phone = input("Enter phone:\n")
    city = input("Enter city:\n")
    state = input("Enter state:\n")

    new_dict = {}

    keys = ['first_name', 'last_name', 'phone', 'city', 'state']
    values = [first_name, last_name, phone, city, state]

    for i in range(5):
        new_dict[keys[i]] = values[i]

    if a is None:
        file_dict_local['person_' + f'{len(file_dict_local) + 1}'] = new_dict
    else:
        file_dict_local[a] = new_dict

    return file_dict_local


def upload_new_info(local_filename, new_info):
    """Изменяет файл json"""
    with open(local_filename, 'w') as f:
        json.dump(new_info, f)


def search_info(name, key):
    """ Функция ищет совпадения заданных значений по ключу. Если совпадений нет, возвращает None.
        Параметры: name - что нужно искать, key - по какому ключу """
    for i in file_dict:
        x = file_dict[i].get(key).lower()
        if name.lower() == x:
            return file_dict[i]


def search_info_key(name, key):
    """ Функция ищет совпадения заданных значений по ключу. Если совпадений нет, возвращает None.
        Параметры: name - что нужно искать, key - по какому ключу
        Возвращает ключ словаря верхнего уровня"""
    for i in file_dict:
        x = file_dict[i].get(key).lower()
        if name.lower() == x:
            return i


def add_new_entries():  # Первый пункт меню!!
    """Функция добавления новых данных в json файл"""
    new_data = formatting(file_dict, None)
    upload_new_info(filename, new_data)


def search_by_first_name():  # Второй пункт меню!!
    name_choice = input("Enter name you want to search by:\n")
    result = search_info(name_choice, 'first_name')
    if result is not None:
        return f"Entry with name {name_choice.title()}: {result}\n"
    else:
        return "There is no entry with such a name\n"


def search_by_last_name():  # Третий пункт меню!!
    last_name_choice = input("Enter last name you want to search by:\n")
    result = search_info(last_name_choice, 'last_name')
    if result is not None:
        return f"Entry with last name {last_name_choice.title()}: {result}\n"
    else:
        return "There is no entry with such a last name\n"


def search_by_full_name():  # Четвёртый пункт меню!!
    list_full_name = input("Enter full name you want to search by in format 'name surname'. For example 'Artem Shestak'"
                           ":\n").split()
    if len(list_full_name) == 2:
        name = list_full_name[0]
        last_name = list_full_name[1]
    else:
        return "Enter 2 exactly 2 words\n"

    result = [search_info(name, 'first_name'), search_info(last_name, 'last_name')]
    if None not in result:
        return f"Entry with full name {name.title()} {last_name.title()}: {result[0]}\n"
    else:
        return "There is no entry with such a full name\n"


def search_by_telephone_number():  # Пятый пункт меню!!
    phone = input("Enter the phone you want to search by:\n")
    result = search_info(phone, 'phone')
    if result is not None:
        return f"Entry with the phone {phone}: {result}\n"
    else:
        return "There is no entry with such a phone\n"


def search_by_city_or_state():  # Шестой пункт меню!!
    city_or_state = input("Enter city or state you want to search by:\n")
    result = [search_info(city_or_state, 'city'), search_info(city_or_state, 'state')]
    if result[0] is not None:
        return f"Entry with city {city_or_state.title()}: {result[0]}\n"
    elif result[1] is not None:
        return f"Entry with state {city_or_state.title()}: {result[1]}\n"
    else:
        return "There is no entry with such city of state\n"


def delete_record_by_number():  # Седьмой пункт меню!!
    phone = input("Enter the phone number. Entry that contains this number will be deleted:\n")
    result = search_info_key(phone, 'phone')
    if result is not None:
        del file_dict[result]
        upload_new_info(filename, file_dict)
        return f"Entry with the {phone} has been deleted!\n"
    else:
        return "There is no entry with such a phone\n"


def update_record_by_number():  # Восьмой пункт меню!!
    phone = input("Enter the phone number. Entry that contains this number will be updated:\n")
    result = search_info_key(phone, 'phone')
    if result is not None:
        formatting(file_dict, result)
        upload_new_info(filename, file_dict)
        return f"Current version of entry is:\n{file_dict[result]}\n\nHere you can update this entry.\n"
    else:
        return "There is no entry with such a phone\n"


class TestPhonebook(unittest.TestCase):
    ann = {
        "first_name": "Ann",
        "last_name": "Smith",
        "phone": "380923331122",
        "city": "Los Angeles",
        "state": "California"
    }
    with open("phonebook.json") as f:
        l_dict = json.load(f)
        tady = l_dict.get("person2")

    def test_search_info(self):
        self.assertEqual(search_info("test", "first_name"), None)
        self.assertEqual(search_info("ann", "first_name"), self.ann)
        self.assertEqual(search_info("3809233245222", "phone"), self.tady)

    def test_search_by_first_name(self):
        print("Напиши какую-то фигню")
        self.assertEqual("There is no entry with such a name\n", search_by_first_name())

    def test_record_by_number(self):
        """Ввести каку-то фигню, например 'dgdsfgds' """
        print("Напиши что попало в следующих тестах")
        self.assertEqual("There is no entry with such a phone\n", delete_record_by_number())
        self.assertEqual("There is no entry with such a phone\n", update_record_by_number())
        self.assertEqual("There is no entry with such city of state\n", search_by_city_or_state())
        self.assertEqual("There is no entry with such a phone\n", search_by_telephone_number())
        print("Здесь нужно ввести 2 рандомных слова")
        self.assertEqual("There is no entry with such a full name\n", search_by_full_name())
        print("Здесь нужно ввести либо 1 слово, либо больше двух")
        self.assertEqual("Enter 2 exactly 2 words\n", search_by_full_name())
        self.assertEqual("There is no entry with such a last name\n", search_by_last_name())
        self.assertEqual("There is no entry with such a name\n", search_by_first_name())
