import json
from typing import Optional


try:
    filename = 'phonebook.json'
    with open(filename) as f:
        file_dict = json.load(f)
except FileNotFoundError:
    print("There is no such a file in current directory")


def formatting(file_dict_local, a: Optional[str]) -> dict:
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


def upload_new_info(local_filename: str, new_info: dict) -> None:
    """Изменяет файл json"""
    with open(local_filename, 'w') as f:
        json.dump(new_info, f)


def search_info(name: str, key: str) -> Optional[dict]:
    """ Функция ищет совпадения заданных значений по ключу. Если совпадений нет, возвращает None.
        Параметры: name - что нужно искать, key - по какому ключу """
    for i in file_dict:
        x = file_dict[i].get(key).lower()
        if name.lower() == x:
            return file_dict[i]
    return None


def search_info_key(name: str, key: str) -> Optional[str]:
    """ Функция ищет совпадения заданных значений по ключу. Если совпадений нет, возвращает None.
        Параметры: name - что нужно искать, key - по какому ключу
        Возвращает ключ словаря верхнего уровня"""
    for i in file_dict:
        x = file_dict[i].get(key).lower()
        if name.lower() == x:
            return i
    return None


def add_new_entries() -> None:  # Первый пункт меню!!
    """Функция добавления новых данных в json файл"""
    new_data = formatting(file_dict, None)
    upload_new_info(filename, new_data)


def search_by_first_name() -> str:  # Второй пункт меню!!
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


def search_by_full_name() -> str:  # Четвёртый пункт меню!!
    list_full_name: list = input("Enter full name you want to search by in format 'name surname'. "
                                 "For example 'Artem Shestak':\n").split()
    name = list_full_name[0]
    last_name = list_full_name[1]

    result = [search_info(name, 'first_name'), search_info(last_name, 'last_name')]
    if None not in result:
        return f"Entry with full name {name.title()} {last_name.title()}: {result[0]}\n"
    else:
        return "There is no entry with such a full name\n"


def search_by_telephone_number() -> str:  # Пятый пункт меню!!
    phone = input("Enter the phone you want to search by:\n")
    result = search_info(phone, 'phone')
    if result is not None:
        return f"Entry with the phone {phone}: {result}\n"
    else:
        return "There is no entry with such a phone\n"


def search_by_city_or_state() -> str:  # Шестой пункт меню!!
    city_or_state = input("Enter city or state you want to search by:\n")
    result = [search_info(city_or_state, 'city'), search_info(city_or_state, 'state')]
    if result[0] is not None:
        return f"Entry with city {city_or_state.title()}: {result[0]}\n"
    elif result[1] is not None:
        return f"Entry with state {city_or_state.title()}: {result[1]}\n"
    else:
        return "There is no entry with such city of state\n"


def delete_record_by_number() -> str:  # Седьмой пункт меню!!
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
