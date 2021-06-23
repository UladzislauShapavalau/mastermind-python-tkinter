from tkinter import Label, Button, Entry, StringVar
from functions import *


class RulesGame:
    """Klasa zawierająca funkcji logiki gry, restarta, sprawdzania reguł oraz rysowania okna"""
    def __init__(self, root):
        """Inicjalizacja zmiennych"""
        self.root = root
        self.textBox = Entry()
        self.hint = Label()
        self.check = Button()
        self.reset = Button()
        self.scammer = Button()
        self.infoBar = Label()
        self.sample = generateSample()
        self.attempts = 0
        self.text = ' '
        self.newHint = ' '
        self.rows = 2
        self.ruleGame = False

    def resetBtn(self):
        """Funkcja restartuje nową grę"""
        self.sample.clear()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.sample = generateSample()
        self.rows = 2
        self.attempts = 0
        self.ruleGame = whatIsRule()
        self.drawField()

    def isScammer(self):
        """Sprawdzanie czy reguły gry są prawidłowe"""
        if self.ruleGame:
            self.infoBar.configure(text='Złapałeś/łas mnie!')
            self.check['state'] = 'disabled'
            self.scammer['state'] = 'disabled'
        else:
            self.infoBar.configure(text=f'Tere fere, {"".join(self.sample)}')
            self.check['state'] = 'disabled'
            self.scammer['state'] = 'disabled'

    def mainLogic(self, txt):
        """Główna logika gry. Liczy i daje odpowiedzi czy gracz poprawnie podał liczby."""
        self.text = txt.get()
        assert isTrueInput(self.text) is True
        self.newHint = ''
        test = []
        if self.ruleGame:
            self.newHint = createFakeFeedback()
        else:
            for i in range(4):
                if self.text[i] == self.sample[i]:
                    self.newHint += 'X'
                    test.append(i)
            lstRows = test.copy()
            for i in range(4):
                for j in range(4):
                    if self.text[i] == self.sample[j] and i not in lstRows and j not in test:
                        self.newHint += 'O'
                        lstRows.append(i)
                        test.append(j)
        self.hint.configure(text=self.newHint)
        if self.newHint == 'XXXX':
            self.infoBar.configure(text='Wygrana!')
            self.check['state'] = 'disabled'
            self.scammer['state'] = 'disabled'
        elif self.attempts > 10:
            self.infoBar.configure(text=f'Przegrana! {"".join(self.sample)}')
            self.check['state'] = 'disabled'
            self.scammer['state'] = 'disabled'
            self.root.unbind('<Return>')
        Label(self.root, text=f'{self.rows - 1}) {self.text} {self.newHint}').grid(row=self.rows, column=0,
                                                                                   columnspan=8, sticky='w', padx=4)
        self.rows += 1
        self.attempts += 1
        self.textBox.delete(0, 'end')

    def drawField(self):
        """Funkcja rysuje okno"""
        text = StringVar()
        self.textBox = Entry(self.root, width=4, textvariable=text, justify='left')
        self.textBox.grid(row=0, column=0, columnspan=4, sticky="e", padx=17, pady=5)
        self.hint = Label(self.root, text='    ')
        self.hint.grid(row=0, column=5, columnspan=4, padx=10, pady=5)
        self.check = Button(self.root, text='Sprawdż', command=lambda t=text: self.mainLogic(t))
        self.reset = Button(self.root, text='Reset', command=self.resetBtn)
        self.scammer = Button(self.root, text='Oszust!', command=self.isScammer)
        self.check.grid(row=0, column=10, columnspan=4, sticky="nsew", padx=17, pady=5)
        self.scammer.grid(row=1, column=10, columnspan=4, sticky="nsew", padx=17, pady=5)
        self.reset.grid(row=2, column=10, columnspan=4, sticky="nsew", padx=17, pady=5)
        self.infoBar = Label(self.root, text='    ')
        self.infoBar.grid(row=1, column=0, columnspan=8)
        self.root.bind('<Return>', lambda event: self.mainLogic(text))
        self.root.bind('<Escape>', lambda event: self.resetBtn())
        self.ruleGame = whatIsRule()
        print(self.sample)
        print(self.ruleGame)
