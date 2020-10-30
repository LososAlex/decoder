import sys
import os
import random


def load_text(filename, flag):
    filename = "data/" + filename
    try:
        with open(filename, 'r') as textFile:
            text = [line for line in textFile]
    except FileNotFoundError as message:
        print('Такого файла по данному пути не существует: ', filename)
        raise SystemExit()
    if flag:
        return text[0].split('   ')
    else:
        return text[0].split()


def save_text(text, file_name):
    ready_text_to_write = ''
    for i in text:
        ready_text_to_write += i
        ready_text_to_write += ' '
    filename = "data/" + file_name + '.txt'
    try:
        with open(filename, 'w') as textFile:
            textFile.write(ready_text_to_write)
    except FileNotFoundError as message:
        print('Такого файла по данному пути не существует: ', filename)
        raise SystemExit()


def statistic(word):
    global de_let
    for i in word.split():
        if i.isdigit():
            if i in stat:
                stat[i] += 1
            else:
                stat[i] = 1
    de_let = stat.copy()


def code_stat_letters(code_text):
    for i in code_text:
        statistic(i)
    lst = []
    for i in stat.items():
        lst.append(i)
    csl = sorted(lst, key=lambda x: x[1], reverse=True)
    return csl


def decode_letters(csl):
    z = 1
    for i in csl:
        de_let[i[0]] = letter_stat[z]
        z += 1


def replace_letters(let1, let2):
    find1 = False
    find2 = False
    for i in de_let.items():
        if i[1] == let1:
            find1 = True
            num1 = i[0]
        elif i[1] == let2:
            find2 = True
            num2 = i[0]
        if find1 and find2:
            break
    temp_let = de_let[num2]
    de_let[num2] = de_let[num1]
    de_let[num1] = temp_let


def decoding(code_text):
    decoded_text = []
    for i in code_text:
        word = ''
        for j in i.split():
            if j.isdigit():
                word += de_let[j]
            else:
                word += j
        decoded_text.append(word)
    return decoded_text


def coding_text(text):
    let_to_num = {}
    new_text = []
    for i in text:
        word = ''
        for j in i:
            if j.isalpha():
                if j not in let_to_num.keys():
                    rand_num = str(random.randrange(1, 100))
                    while rand_num in let_to_num.values():
                        rand_num = str(random.randrange(1, 100))
                    let_to_num[j] = rand_num
                    word += rand_num + ' '
                else:
                    word += let_to_num[j] + ' '
            else:
                word += j + ' '
        word += '  '
        new_text.append(word)
    return new_text

stat = {}
letter_stat = {1: 'о',
               2: 'е',
               3: 'а',
               4: 'и',
               5: 'н',
               6: 'т',
               7: 'с',
               8: 'р',
               9: 'в',
               10: 'л',
               11: 'к',
               12: 'м',
               13: 'д',
               14: 'п',
               15: 'у',
               16: 'я',
               17: 'ы',
               18: 'ь',
               19: 'г',
               20: 'з',
               21: 'б',
               22: 'ч',
               23: 'й',
               24: 'х',
               25: 'ж',
               26: 'ш',
               27: 'ю',
               28: 'ц',
               29: 'щ',
               30: 'э',
               31: 'ф',
               32: 'ъ',
               33: 'ё'}
de_let = stat.copy()
name = False
decode = False
while True:
    if name:
        print('Введенный файл:', name)
    print('Доступные команды:\n1. Расшифровать текст\n2. Зашифровать текст\n3. Закончить работу')
    command = input('Введите команду: ')
    if command == '1':
        decode = True
        name = input('Введите название файла формата txt: ')
        name = name + '.txt'
        code_text = load_text(name, decode)
        decode_letters(code_stat_letters(code_text))
        while True:
            txt = decoding(code_text)
            print(*txt)
            print('Доступные команды:\n1. Заменить буквы между собой\n2. Сохранить текст в файл\n3. Закончить работу')
            while True:
                command = input('Введите номер комманды: ')
                if command == '1':
                    l1, l2 = input('Введите буквы через пробел: ').split()
                    replace_letters(l1, l2)
                    break
                elif command == '2':
                    name_of_file = input('Введите название файла, куда вы хотите сохранить текст: ')
                    save_text(txt, name_of_file)
                    break
                elif command == '3':
                    exit()
                else:
                    print('Неправильный ввод команды. Повторите попытку')
    elif command == '2':
        decode = False
        name = input('Введите название файла формата txt: ')
        name = name + '.txt'
        text = load_text(name, decode)
        coding_txt = coding_text(text)
        name_of_file = input('Введите название файла, куда вы хотите сохранить текст: ')
        save_text(coding_txt, name_of_file)
        print('Готово')
    elif command == '3':
        exit()
    else:
        print('Неправильный ввод команды. Повторите попытку')

