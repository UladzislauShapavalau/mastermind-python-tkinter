from tkinter import Tk
from game import *
import unittest
import random


class TestProject(unittest.TestCase):
    root = Tk()
    game = RulesGame(root)
    game.drawField()

    # def test_0_checkIfNotGuessed(self):
    #     """Wpisanie odpowiedzi z błędymi cyframi"""
    #     self.game.ruleGame = False
    #     entry = StringVar(self.root, "1111")
    #     response = "Przegrana!"
    #
    #     for i in range(12):
    #         self.game.mainLogic(entry)
    #
    #     self.assertTrue(response in self.root.children[f'!label4'].cget('text'))
    #
    # #
    # def test_1_checkIfTwoNumbersAreCorrect(self):
    #     """Wpisywanie odpowiedzi z dwoma poprawnymi cyframi w złych miejscach"""
    #     self.game.ruleGame = False
    #     testSample = self.game.sample[:]
    #     if testSample[2] == '1':
    #         firstNum = '2'
    #     elif testSample[2] == '6':
    #         firstNum = '5'
    #     else:
    #         firstNum = str(int(testSample[2]) + 1)
    #
    #     if testSample[3] == '1':
    #         secondNum = '2'
    #     elif testSample[3] == '6':
    #         secondNum = '5'
    #     else:
    #         secondNum = int(testSample[3]) + 1
    #
    #     testSample.pop()
    #     testSample.pop()
    #     test = "".join(testSample)
    #     entry = StringVar(self.root, f"{firstNum}{secondNum}{test}")
    #     response = "OO"
    #     self.game.mainLogic(entry)
    #
    #     print(self.root.children[f'!label3'].cget('text'))
    #
    #     self.assertTrue(response in self.root.children[f'!label3'].cget('text'))

    def test_2_checkIfNumbersAreCorrect(self):
        """Wpisywanie odpowiedzi z poprawnymi cyframi w
        złych miejscach oraz dobrych miejscach."""
        self.game.ruleGame = False
        testSample = self.game.sample[:]

        testSample[0], testSample[-1] = testSample[-1], testSample[0]
        test = "".join(testSample)
        entry = StringVar(self.root, f"{test}")
        response = "XO"
        self.game.mainLogic(entry)

        print(self.root.children[f'!label3'].cget('text'))

        self.assertTrue(response in self.root.children[f'!label3'].cget('text'))

    # def test_3_checkIfGuessed(self):
    #     """Wpisywanie poprawnej odpowiedzi"""
    #     self.game.ruleGame = False
    #     testSample = self.game.sample[:]
    #
    #     test = "".join(testSample)
    #     entry = StringVar(self.root, f"{test}")
    #     response = "Wygrana!"
    #
    #     self.game.mainLogic(entry)
    #
    #     self.assertTrue(response in self.root.children[f'!label4'].cget('text'))

    # def test_4_checkIfValidInput(self):
    #     """Wpisywanie niepoprawnego kodu (więcej niż 4 znaki)"""
    #     self.game.ruleGame = False
    #     test = "1231231"
    #     entry = StringVar(self.root, f"{test}")
    #
    #     self.assertRaises(AssertionError, self.game.mainLogic, entry)

    # def test_5_checkIfValidInput(self):
    #     """Wpisywanie niepoprawnego kodu (znaki nie będące cyframi od 1 do 6)"""
    #     self.game.ruleGame = False
    #     test = "8779"
    #     entry = StringVar(self.root, f"{test}")
    #
    #     self.assertRaises(AssertionError, self.game.mainLogic, entry)


    # def test_6_checkIfScammer(self):
    #     """Wciśnięcie przycisku "Oszust!" pry niepoprawnych zasadach gry"""
    #     self.game.ruleGame = True
    #     response = 'Złapałeś/łas mnie!'
    #
    #     button = self.root.children['!button6']
    #     button.invoke()
    #
    #     self.assertTrue(response in self.root.children[f'!label4'].cget('text'))

    # def test_7_checkIfScammer(self):
    #     """Wciśnięcie przycisku "Oszust!" pry poprawnych zasadach gry"""
    #     self.game.ruleGame = False
    #     response = 'Tere fere'
    #
    #     button = self.root.children['!button6']
    #     button.invoke()
    #
    #     self.assertTrue(response in self.root.children[f'!label4'].cget('text'))

if __name__ == '__main__':
    unittest.main()