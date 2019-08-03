import time
import random


def GameInrto():
    print('You awake in a overgrown grotto')
    time.sleep(3)
    print('You dont know who you are.......')
    time.sleep(2)
    print('or how you got here')
    print('In front of you you see two caves.'
          'In one cave lies a kind dragon that will share his treasure with you.'
          'The other is greedy and will kill you if given the chance.''')


def chooseCave():
    cave = ""
    while cave != '1' and cave != '2':
        print('which cave will you venture down? (1 or 2)')
        cave = input()
        return cave


def checkCave(chooseCave):
    print('You approach the cave of your choice......')
    time.sleep(2)
    print('You approach the cave of your choice......')
