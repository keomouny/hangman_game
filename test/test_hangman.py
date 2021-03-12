#!/usr/bin/env python3

import unittest
import os
from pendu_game.hangman import HangmanGame


class TestHangman(unittest.TestCase):

    def test_get_word(self):
        hangman_game = HangmanGame()
        hangman_game.get_word()
        self.assertTrue(os.path.exists('liste_francais.txt'))
        self.assertIs(type(hangman_game.random_word), str)
        self.assertIs(type(hangman_game.randomToList), list)

    def test_create_hangman(self):
        hangman_game = HangmanGame()
        hangman_game.create_hangman()
        self.assertEqual(len(hangman_game.scaffold), 7)
        self.assertIs(type(hangman_game.scaffold), list)

    def test_convert_word_underscore(self):
        hangman_game = HangmanGame()
        hangman_game.get_word()
        hangman_game.convert_word_underscore(hangman_game.randomToList)
        self.assertIs(type(hangman_game.word_hidden), list)


if __name__ == '__main__':
    unittest.main(verbosity=2)
