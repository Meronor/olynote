import sqlite3
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


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
        print(get_url)
        return False


def get_note(olimp, email):
    try:
        with sqlite3.connect("datausers") as con:
            cur = con.cursor()
            return cur.execute(f"SELECT `{olimp}` FROM notes1 WHERE id='{email}'").fetchall()[0][0]
    except Exception:
        print('get_note')
        return False


def set_note(olimp, note, email):
    with sqlite3.connect("datausers") as con:
        cur = con.cursor()
        try:
            cur.execute(f'UPDATE notes1 SET `{olimp}` = "{note}" WHERE id = "{email}"')
        except Exception:
            print('set_note')
        return False


def handle_link_activation(url):
    QDesktopServices.openUrl(QUrl(url))
