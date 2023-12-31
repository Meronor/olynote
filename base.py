import sqlite3
import datetime
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QStyleFactory


def get_dates():
    try:
        with sqlite3.connect("datausers") as con:
            cur = con.cursor()
            return list(map(lambda x: x[0], cur.execute(f"SELECT date FROM dates").fetchall()))
    except Exception as s:
        print(s)
        print('get_dates')
        return False

def theme(wind, color):
    if color == 'light':
        print(1)
        wind.setStyle(QStyleFactory.create("Fusion"))
    else:
        print(2)
        wind.setStyleSheet("background-color: #2b2b2b")
        wind.setStyleSheet("QPushButton { background-color: #dbdbdb }")


def add_user(email, password):
    with sqlite3.connect("datausers") as con:
        cur = con.cursor()
        try:
            if len(password) <= 7:
                return 'Your password has less than 7 symbols'
            if password.isdigit():
                return 'Use at least 1 letter in password'
            if password.isalpha():
                return 'Use at least 1 digit in password'
            if len(email) < 5 or '@' not in email or '.' not in email:
                return 'Wrong email'

            inornot = cur.execute(f"SELECT * FROM users WHERE email='{email}'").fetchall()
            if len(inornot) == 0:
                cur.execute(f"INSERT INTO users (email, password) VALUES ('{email}', '{password}')")
                cur.execute(f"INSERT INTO notes1 (id) VALUES ('{email}')")
                return True
        except Exception as e:
            print(e)
            print('add_user')
        return 'email is yet'


def get_url(olimp):
    try:
        with sqlite3.connect("datausers") as con:
            cur = con.cursor()
            return cur.execute(f"SELECT `{olimp}` FROM notes1 WHERE id='0'").fetchall()[0][0]
    except Exception as s:
        print(s)
        print('get_url')
        return False


def get_olys():
    try:
        with sqlite3.connect("datausers") as con:
            cur = con.cursor()
            return list(map(lambda x: x[0], cur.execute(f"SELECT olimp FROM notes").fetchall()))
    except Exception as s:
        print(s)
        print('get_olys')
        return False


def get_note(olimp, email):
    try:
        with sqlite3.connect("datausers") as con:
            cur = con.cursor()
            return cur.execute(f"SELECT `{olimp}` FROM notes1 WHERE id='{email}'").fetchall()[0][0]
    except Exception as s:
        print(s)
        print('get_note')
        return False


def get_theme(email):
    try:
        with sqlite3.connect("datausers") as con:
            cur = con.cursor()
            return cur.execute(f"SELECT theme FROM notes1 WHERE id='{email}'").fetchall()[0][0]
    except Exception as s:
        print(s)
        print('email')
        return False


def get_event(email, date):
    try:
        with sqlite3.connect("datausers") as con:
            cur = con.cursor()
            ret = []
            for name, time in cur.execute(
                    f"SELECT name, time FROM dates WHERE user='{email}' AND date = '{date}' ORDER BY time").fetchall():
                ret.append((name, datetime.time(time // 60, time % 60).strftime('%H:%M')))
            return ret
    except Exception as s:
        print(s)
        print('get_event')
        return False


def set_theme(color, email):
    with sqlite3.connect("datausers") as con:
        cur = con.cursor()
        try:
            cur.execute(f'UPDATE notes1 SET theme = "{color}" WHERE id = "{email}"')
        except Exception as s:
            print(s)
            print('set_theme')
        return False


def set_note(olimp, note, email):
    with sqlite3.connect("datausers") as con:
        cur = con.cursor()
        try:
            cur.execute(f'UPDATE notes1 SET `{olimp}` = "{note}" WHERE id = "{email}"')
        except Exception as s:
            print(s)
            print('set_note')
        return False


def set_date(user, date, name, time):
    with sqlite3.connect("datausers") as con:
        cur = con.cursor()
        try:
            time = int(time.split('.')[0]) * 60 + int(time.split('.')[1])
            cur.execute(f"INSERT INTO dates (user, date, name, time) VALUES ('{user}', '{date}', '{name}', {time})")
        except Exception as s:
            print(s)
            print('set_date')
        return False


def handle_link_activation(url):
    QDesktopServices.openUrl(QUrl(url))
