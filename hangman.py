import random
import os
from pendu_game.setup_logger import logger, path_file_current


class HangmanGame:

    def __init__(self):
        self.scaffold = []
        self.word_hidden = []
        self.randomToList = []
        self.count = 0
        self.finding_letter = None
        self.random_word = None

    def get_word(self):
        try:
            logger.info('open file (list_francais.txt)')
            allText = open(
                f'{path_file_current}/files/liste_francais.txt', 'r').read()
        except:
            logger.error('file not found')
            print('erreur fichier non trouvé')
        else:
            logger.info('get file is ok')
            words = list(map(str, allText.split()))
            self.random_word = random.choice(words)
            self.randomToList = list(self.random_word)
            print(f'random_words = {self.random_word}')

    # create hangman

    def create_hangman(self):
        logger.info('create hangman for hangman game')
        self.scaffold.append('     ==========Y===')
        self.scaffold.append('    ||  /      |')
        self.scaffold.append('    || /       |')
        self.scaffold.append('    ||/        O')
        self.scaffold.append('    ||        /|\\')
        self.scaffold.append('    ||        / \\')
        self.scaffold.append('    ||\n'
                             '   /||\n'
                             '  //||\n'
                             '============')

    # for showing hangman
    def display_hangman(self, nb):
        logger.info('showing part of hangman per error checked')
        for i in range(nb):
            print(self.scaffold[i])
        if self.count > (len(self.scaffold) - 1):
            print('you lose..')

    # create word hidden
    def convert_word_underscore(self, word):
        logger.info('convert word from liste_francais file to underscore list')
        word_h = '_ ' * len(word)
        self.word_hidden = word_h[:-1].split(' ')
        print(f'your word hidden is = {self.word_hidden}')

    # check letter from random word
    def checkLetter(self, letter):
        logger.info(f'check letter = {letter} in checkLetter method')
        print('randomword', self.random_word)
        if letter in self.random_word:
            print(f'great you finding letter {letter} from random_word')
            self.finding_letter = letter
        else:
            self.count += 1
            print(f'count = {self.count}')
            self.display_hangman(self.count)

    # add letter in word to finding
    def add_letter_in_word(self, letter):
        logger.info('adding letter in underscore word list')
        for i in range(len(self.randomToList)):
            if letter == self.randomToList[i]:
                self.word_hidden[i] = letter
        print(f'word hidden = {self.word_hidden}')
        print(f'randomlist {self.randomToList}')

    # launch game
    def launch_game(self):
        logger.info('launch hangman game')
        self.create_hangman()
        self.get_word()
        self.convert_word_underscore(self.randomToList)
        while self.count <= (len(self.scaffold) - 1):
            if ''.join(self.word_hidden) != self.random_word:
                self.checkLetter(input('Choose your letter : \n').lower())
                self.add_letter_in_word(self.finding_letter)
                print(' '.join(self.word_hidden))
            else:
                print('Great you have found hidden word completly')
                break
