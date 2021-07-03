def caesar_cipher(l_message, l_offset, l_lang, mode='encode'):
    alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    message = l_message.upper()
    offset = l_offset  # int(input('Шаг: '))
    lang = l_lang.lower()  # input('Выберите язык RU/EU: ').lower()

    def process(alphabet):
        result = ''

        for i in message:
            index = alphabet_ru.find(i)
            if mode == 'encode':
                new_index = index + offset
            elif mode == 'decode':
                new_index = index + offset
            else:
                raise Exception('Выбран некорректный mode')
            if i in alphabet_ru:
                result += alphabet[new_index]
            else:
                result += i

        return result

    if lang == 'ru':
        final_result = process(alphabet_ru)
    elif lang == 'en':
        final_result = process(alphabet_en)
    else:
        raise Exception('Выбран некорректный язык')

    return final_result
