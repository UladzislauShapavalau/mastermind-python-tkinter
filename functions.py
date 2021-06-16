from random import choice, randint, choices
from tkinter import messagebox


def isTrueInput(text):
    if len(str(text)) == 4:
        for i in str(text):
            try:
                if int(i) < 1 or int(i) > 6:
                    messagebox.showerror('Invalid input', 'Numbers must be > 0 and < 7')
                    return False
            except ValueError:
                messagebox.showerror('Invalid input', 'Type must be integer')
                return False
        return True
    else:
        messagebox.showerror('Invalid input', 'Length must be 4')
        return False

"""Generuje losowe liczbe"""
def generateSample():
    return [choice('123456') for _ in range(4)]

"""Wybór zestawu reguł"""
def whatIsRule():
    return choice([True, False])

"""Generuje niepoprawne odpowiedzi"""
def createFakeFeedback():
    amount = randint(1, 3)
    text = choices(['X', 'O'], weights=(4, 6), k=amount)
    return ''.join(sorted(text, reverse=True))

"""Blokuje przeciski"""
def disableButtons(*args):
    for i in args:
        i['state'] = 'disabled'
