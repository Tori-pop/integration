'''
This file holds the game assets to design the aesthetic of the game.
author = Victoria Poplawski
'''
import time
import sys


def text(s):
    '''
    :param s: game dialogue
    :return: single character printed to console at a rate of 25 mil sec
    '''
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)


def textSlow(s):
    '''
      :param s: game dialogue
      :return: single character printed to console at a rate of 100 mil sec
      '''
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


def textFast(s):
    '''
      :param s: game dialogue
      :return: single character printed to console at a rate of 10 mil sec
      '''
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


def printAssChoice(i_num):
    '''
    :param i_num: number of '*' wanted
    :return: Rows of increasing lens of '*' depending on input
    '''
    for row in range(i_num):
        for column in range(7):
            print("*", end=" ")
        print()


def printAss():
    '''
    :return: Rows of increasing lens of '*'
    '''
    for row in range(1, 10):
        for column in range(row):
            textFast("*    ")
        print()
