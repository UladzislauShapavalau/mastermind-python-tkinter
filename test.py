from tkinter import Tk
from game import *
import unittest
import random


class TestProject(unittest.TestCase):
    root = Tk()
    game = RulesGame(root)
    game.drawField()

    def test_0_checkIfNotGuessed(self):
        """Wpisanie odpowiedzi z błędymi cyframi"""
        self.game.ruleGame = False
        self.game.sample = ['2', '2', '2', '2']
        entry = StringVar(self.root, "1111")
        response = "Przegrana!"

        for i in range(12):
            self.game.mainLogic(entry)

        self.assertTrue(response in self.root.children[f'!label4'].cget('text'))


    def test_1_checkIfTwoNumbersAreCorrect(self):
        """Wpisywanie odpowiedzi z dwoma poprawnymi cyframi w złych miejscach"""
        self.game.ruleGame = False
        self.game.sample = ['1', '2', '3', '4']

        entry = StringVar(self.root, f"3466")
        response = "OO"
        self.game.mainLogic(entry)

        print(self.root.children[f'!label3'].cget('text'))

        self.assertTrue(response in self.root.children[f'!label3'].cget('text'))

    def test_2_checkIfNumbersAreCorrect(self):
        """Wpisywanie odpowiedzi z poprawnymi cyframi w
        złych miejscach oraz dobrych miejscach."""
        self.game.ruleGame = False
        self.game.sample = ['1', '2', '3', '4']
        print(self.game.sample)

        entry = StringVar(self.root, f"1243")
        response = "XXOO"
        self.game.mainLogic(entry)

        print(self.root.children[f'!label3'].cget('text'))

        self.assertTrue(response in self.root.children[f'!label3'].cget('text'))

    def test_3_checkIfGuessed(self):
        """Wpisywanie poprawnej odpowiedzi"""
        self.game.ruleGame = False
        testSample = self.game.sample[:]

        test = "".join(testSample)
        entry = StringVar(self.root, f"{test}")
        response = "Wygrana!"

        self.game.mainLogic(entry)

        self.assertTrue(response in self.root.children[f'!label4'].cget('text'))

    def test_4_checkIfValidInput(self):
        """Wpisywanie niepoprawnego kodu (więcej niż 4 znaki)"""
        self.game.ruleGame = False
        test = "1231231"
        entry = StringVar(self.root, f"{test}")

        self.assertRaises(AssertionError, self.game.mainLogic, entry)

    def test_5_checkIfValidInput(self):
        """Wpisywanie niepoprawnego kodu (znaki nie będące cyframi od 1 do 6)"""
        self.game.ruleGame = False
        test = "8779"
        entry = StringVar(self.root, f"{test}")

        self.assertRaises(AssertionError, self.game.mainLogic, entry)


    def test_6_checkIfScammer(self):
        """Wciśnięcie przycisku "Oszust!" pry niepoprawnych zasadach gry"""
        self.game.resetBtn()
        self.game.ruleGame = True
        response = 'Złapałeś/łas mnie!'

        button = self.root.children['!button9']
        button.invoke()

        self.assertTrue(response in self.root.children[f'!label21'].cget('text'))

    def test_7_checkIfScammer(self):
        """Wciśnięcie przycisku "Oszust!" pry poprawnych zasadach gry"""
        self.game.resetBtn()
        self.game.ruleGame = False
        response = 'Tere fere'

        button = self.root.children['!button12']
        button.invoke()

        self.assertTrue(response in self.root.children[f'!label23'].cget('text'))

    def test_8_checkReset(self):
        """Wpisanie 10 odpowiedzi z błędymi cyframi. Wciśnięcie "Reset".
        Wpisanie 5 odpowiedzi z błędymi cyframi. Sprawdzanie czy licznik tur
        resetuje po wciścnięciu "Reset" """
        self.game.ruleGame = False
        self.game.sample = ['2', '2', '2', '2']
        entry = StringVar(self.root, "1111")
        response = 5

        for i in range(10):
            self.game.mainLogic(entry)

        self.game.resetBtn()

        for i in range(5):
            self.game.mainLogic(entry)

        self.assertEqual(response, self.game.attempts)


if __name__ == '__main__':
    unittest.main()