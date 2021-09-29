from shutil import copy
from datetime import date, timedelta
from ctypes import *
from os import listdir
from os.path import isfile, join

windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
setclr = windll.Kernel32.SetConsoleTextAttribute

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
    with open('copied.txt', 'r') as copied:
        for line in copied:
            if fn == line.strip():
                return True
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
            setclr(h, 10)
            print("СКОПИРОВАЛ "+fn)
            with open('copied.txt', 'a') as f:
                f.write(fn+'\n')
        except:
            setclr(h, 12)
            print('!НЕ СКОПИРОВАЛОСЬ :-(')
def check_last_week():
    onlyfiles = [f for f in listdir(src) if isfile(join(src, f))]
    print(onlyfiles)
    print(len(onlyfiles))



#src = '\\\\Bam\\D$\\Bill\\Bill\\'
#dst = '\\\\10.149.105.2\\data\\in\\'
archive = '\\\\10.149.105.2\\data\\archive\\'
src = 'D:\\'
dst = 'D:\I\\'

setclr(h, 7)
#copy_day(fnc(1))

check_last_week()

while True:

    if input() == 'exit':
        break
setclr(h, 7)