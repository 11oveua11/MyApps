from shutil import copy
from datetime import date, timedelta
from ctypes import *
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
for color in range(16):
    setclr = windll.Kernel32.SetConsoleTextAttribute
    setclr(h, color)


def fnc(days_ago):
    '''File Name Constructor.
    Коструктор имени файла.
    1 аргумент - days_ago - количество прошедших дней'''
    file = (date.today() - timedelta(days=days_ago)).strftime('20%y%m%d.BIL')
    return file

def wfc(fn):
    '''Was file copied?
    Проверка, был ли файл ранее скопирован?
    1 аргумент - fn - имя файла'''
    with open('copied.txt') as copied:
        lst_of_files = [line for line in copied]
        if fn in lst_of_files:
            return True
        else:
            return False

def copy_day(fn):
    'копиирование файла'
    if wfc(fn):
        setclr(h, 11)
        print('файл '+fn+' уже копировал')
    else:
        try:
            setclr(h, 14)
            print("попытка скопировать: "+fn+", жди...\nИЗ: "+src+"\nВ: "+dst)
            copy(src + fn, dst + fn)
            print("СКОПИРОВАЛ "+fn)
            with open('copied.txt', 'a') as f:
                f.write(fn+'\n')
        except:
            print('!НЕ СКОПИРОВАЛОСЬ :-(')

#src = '\\\\10.149.105.2\\data\\in\\'
#dst = '\\\\Bam\D\\Bill\\Bill\\'
src = 'c:\\Users\\Adm\\Desktop\\'
dst = 'd:\\'

copy_day(fnc(1))

while True:
    if input() == 'exit':
        break
