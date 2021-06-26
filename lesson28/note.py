import os
import time


def open_file(filename):
    try:
        with open(filename, 'r') as file_object:
            lines = file_object.readlines()
        return lines
    except FileNotFoundError:
        return None


def upload_new_info(local_filename: str, new_info: str) -> None:
    with open(local_filename, 'w') as f:
        f.write(new_info)


def find(name: str):
    text = open_file(f'{name}.txt')
    if text:
        return text[0]
    else:
        return "There is no such a Note"


def del_note(name: str):
    try:
        os.remove(f'{name}.txt')
    except FileNotFoundError:
        return "Такой заметки не существует"


class Note:
    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text

        upload_new_info(f'{name}.txt', f'Note text: "{text}". Created time - {time.strftime("%D - %H:%M")}')

    @staticmethod
    def change_note(name: str):
        text = open_file(f'{name}.txt')
        local_text = text[0]
        print(f'Текущая запись: "{local_text}"')
        question1 = input("Что вы хотите изменить?\n")
        if question1 in text[0]:
            question2 = input("На что вы хотите изменить?\n")
            final_text = local_text.replace(question1, question2)
            upload_new_info(f'{name}.txt', f'Note text: "{final_text}". Edited time - {time.strftime("%D - %H:%M")}')
            print(final_text)
        else:
            print("Некорректный ввод")


new_note = Note('breakfast', 'eggs, salad, water')
new_note.change_note('breakfast')

# print(find('breakfast'))
