from tkinter import Label, Button, Entry, StringVar
from random import choice


class RulesGame:
    def __init__(self, root):
        self.root = root
        self.textBox = Entry()
        self.hint = Label()
        self.check = Button()
        self.reset = Button()
        self.scammer = Button()
        self.infoBar = Label()
        self.sample = [choice('123456') for _ in range(4)]
        self.attempts = 0
        self.text = ' '
        self.newHint = ' '

    def printWrongAnswer(self, text, newHint):
        pass

    def drawField(self):
        pass


class AlgorithmGame(RulesGame):
    def __init__(self, root):
        RulesGame.__init__(self, root)
        self.rows = 2

    def checkText(self, txt):
        self.text = txt.get()
        self.newHint = ''
        test = []
        for i in range(4):
            if self.text[i] == self.sample[i]:
                self.newHint += 'X'
                test.append(i)

        lstRows = test.copy()
        for i in range(4):
            for j in range(4):
                if self.text[i] == self.sample[j] and i not in lstRows and j not in test:
                    self.newHint += '0'
                    lstRows.append(i)
                    test.append(j)
        self.hint.configure(text=self.newHint)
        self.attempts += 1
        if self.newHint == 'XXXX':
            self.infoBar.configure(text='Wygrana!')
        elif self.attempts > 12:
            self.infoBar.configure(text=f'Przegrana! {self.sample}')
        Label(self.root, text=f'{self.rows - 1}) {self.text} {self.newHint}').grid(row=self.rows, column=0,
                                                                                   columnspan=8, sticky='w', padx=4)
        self.rows += 1
        #for widget in self.root.grid_slaves():
            #if int(widget.grid_info()["row"]) < 1:
         #       widget.destroy()
        #self.drawField()

    def drawField(self):
        text = StringVar()
        self.textBox = Entry(self.root, width=4, textvariable=text, justify='left')
        self.textBox.grid(row=0, column=0, columnspan=4, sticky="e", padx=17, pady=5)
        self.hint = Label(self.root, text='    ')
        self.hint.grid(row=0, column=5, columnspan=4, padx=10, pady=5)
        self.check = Button(self.root, text='Sprawdż', command=lambda t=text: self.checkText(t))
        self.reset = Button(self.root, text='Reset')
        self.scammer = Button(self.root, text='Oszust!')
        self.check.grid(row=0, column=10, columnspan=4, sticky="nsew", padx=17, pady=5)
        self.scammer.grid(row=1, column=10, columnspan=4, sticky="nsew", padx=17, pady=5)
        self.reset.grid(row=2, column=10, columnspan=4, sticky="nsew", padx=17, pady=5)
        self.infoBar = Label(self.root, text='    ')
        self.infoBar.grid(row=1, column=0, columnspan=8)
        self.infoBar.configure(text=self.sample)
        self.root.bind('<Return>', lambda event: self.checkText(text))

# class WrongAnswers(RulesGame):
#     def __init__(self, root, text, newHint):
#         super().__init__(root)
#         self.iteration = 1
#         self.rows = 2
#         self.root = root
#         self.text = text
#         self.newHint = newHint
#
#     def printWrongAnswer(self, text, newHint):
#         Label(self.root, text=f'{self.iteration}) {self.text} {self.newHint}').grid(row=self.rows, column=0,
#                                                                                     columnspan=8)
#         self.iteration += 1
#         self.rows += 1
