''' unixtime.py - 現在と1週間前のunixtimeを得る関数を記述するモジュール '''

from datetime import datetime, timedelta

def currentunixtime():
    ''' 現在のunixtimeをint形式で得る '''
    now = datetime.now()
    return int(now.strftime('%s'))

def agounixtime(days=0, hours=0, minutes=0):
    ''' 指定されたdays, hours, minitesだけ以前のunixtimeをint形式で得る '''
    delta = timedelta(days=days, hours=hours, minutes=minutes)
    t = datetime.now() - delta
    return int(t.strftime('%s'))

def aweekunixtime():
    ''' 1週間前のunixtimeをint形式で得る '''
    return agounixtime(days=7)







