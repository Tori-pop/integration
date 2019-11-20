import time
import sys


def dell(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

def dellslow(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def dellfast(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


def ass1(i_num):
    for row in range(i_num):
        for column in range(7):
            print("*", end=" ")
        print()


def ass2():
    for row in range(1, 10):
        for column in range(row):
            dellfast("*    ")
        print()
