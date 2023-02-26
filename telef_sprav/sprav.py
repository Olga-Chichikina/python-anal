import sys
from datetime import datetime  as dt
import os.path
import csv


def write_csv_txt_file():
    if not os.path.exists('data.csv'):
        with open ('data.csv', 'w', encoding='utf-8') as dt: 
            st = csv.writer(dt, delimiter = ";")
            st.writerow(('surname','name', 'phone','info'))
    res = ''
    if  res != 'q':
        data_user = [
            (input('Введите фамилию '), input('Введите имя  '), input('Введите номер телефона   '), input('Введите информацию  '))
        ]
        with open ('data.csv', 'a', encoding = 'utf-8') as dt:
            st = csv.writer(dt, delimiter = ";")
            st.writerow(data_user)
            log_info(1)
        file = 'data.txt'
        with open (file, 'a', encoding = 'utf-8') as dt1:
            dt1.write(f'{data_user}\n')
        
def read_txt_file():
    with open ('data.txt', 'r', encoding = 'utf-8') as f:
            data = f.read()
            return data

def read_csv_file():
    with open('data.csv', encoding='utf-8') as f:
        data = []
        st = f.readlines()
        for i in st:
            st_in = i.split(';')
            tpl = tuple(j.strip() for j in st_in)
            data.append(tpl)
            return data

def log_info (act):
    action = ''
    if act == 1:
        action = 'record'
    if act == 2:
        action = 'read'    
    time = dt.now().strftime ("%d %B %Y (%A)")
    with open ('loger.txt', 'a', encoding = 'utf-8') as rec:
        rec.write(f"{action} \n {time}\n")

def find_surname():
    daty = read_txt_file()
    ls = daty.split(")")
    find = input('Введите фамилию: ')
    for elem in ls:
        if find in elem:
            print(elem)

def find_phone():
    daty = read_txt_file()
    ls = daty.split(")")
    find = input('Номер телефона: ')
    for elem in ls:
        if find in elem:
            print(elem)
 

def find_name():
    daty = read_txt_file()
    ls = daty.split(")")
    find = input('Введите Имя: ')
    for elem in ls:
        if find in elem:
            print(elem)

def button_click():
    print ('\nДОБРО ПОЖАЛОВАТЬ В ТЕЛЕФОННУЮ КНИГУ')
    m = -1  
    while m != 0:
        print ('\nПожалуйста, выберите один из следующих пунктов:')  
        print('1. Добавить новый контакт')  
        print('2. Показать контакты')  
        print('3. Поиск по фамилии')
        print('4. Поиск по номеру телефона')
        print('5. Поиск по имени')
        print('0. Выйти из телефонной книги')
        m = int(input('Ваш выбор: '))  
        if m == 1:  
            write_csv_txt_file()
            print('Новый контакт добавлен в книгу')
            continue
        elif m == 2: 
            daty = read_txt_file()
            log_info(2)
            ls = daty.split(")")
            for elem in ls:
                print(*elem)
            continue
        elif m == 3:  
            find_surname()
            continue
        elif m == 4:
            find_phone()
            continue
        elif m == 5:
            find_name()
        elif m == 0:  
            print('Программа завершена.\n')
            sys.exit(0)  
        else:  
            print('Пожалуйста следуйте инструкции')


button_click()