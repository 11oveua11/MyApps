from shutil import copy
from datetime import date, timedelta, datetime
from time import sleep
from ctypes import *
from os import listdir
from os.path import isfile, join

windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
setclr = windll.Kernel32.SetConsoleTextAttribute

def check_archive():
    return [f[29:37]+'.PUS' for f in listdir(archive) if isfile(join(archive, f))]

def fnc(days_ago):
    '''File Name Constructor.
    Коструктор имени файла.
    1 аргумент - days_ago - количество прошедших дней'''
    filename = (date.today() - timedelta(days=days_ago)).strftime('%y-%m-%d.PUS')
    return filename

def copy_day(fn):
    'копиирование файла'
    if fn in all_copied_files:
        setclr(h, 11)
        print('файл '+fn+' уже найден в архиве')
        return True
    else:
        try:
            setclr(h, 14)
            print("копирую: "+fn+"  |  ИЗ: "+src+"  |  В: "+dst+'\nжди...', end='\r')
            copy(src + fn, dst + fn)
            setclr(h, 10)
            print("СКОПИРОВАЛ "+fn)
            return True
        except:
            setclr(h, 12)
            print('!НЕ СКОПИРОВАЛОСЬ :-(  |  Проверь доступ к СПУС или наличие файла')
            return False

src = 'C:\\LinkCPU\\44\\Pus\\'
dst = 'Y:\\in\\'
archive = 'Y:\\archive\\'
#src = 'F:\\' #для тестирования работы скрипта
#dst = 'F:\I\\' #для тестирования работы скрипта

setclr(h, 7)
all_copied_files = check_archive()
last_try = True

if all([copy_day(fnc(i)) for i in range(7, 0, -1)]): #попытка скопировать последнюю неделю
    setclr(h, 10)
    print('Файлы за последнюю неделю были проверены. Всё ОК')
else:
    setclr(h, 12)
    print('Файлы за последнюю неделю были проверены.\nВнимание, не все файлы есть в архиве. Копировать отсутствующие не удалось.')

this_day = datetime.today().day
while True:
    now_event = datetime.now().strftime('%d %b, %H:%M')
    setclr(h, 11)
    print('Последняя проверка была {} ждём следующий день...'.format(now_event), end='\r')
    sleep(7200)
    if this_day != datetime.today().day or last_try is False:
        last_try = copy_day(fnc(1))
    else: pass
    this_day = datetime.today().day
    setclr(h, 7)
