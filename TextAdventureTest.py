import time
import random


def GameInrto():
    print('You awake in a overgrown grotto')
    time.sleep(2)
    print('You dont know who you are.......')
    time.sleep(3)
    print('or how you got here')
    time.sleep(1)
    print('In front of you you see two caves.\n')
    time.sleep(1)
    print('In one cave lies a kind dragon that will share his treasure with you.\n'
          'The other is greedy and will kill you if given the chance.\n')


def describeCaves():
    print('To your left is a gash cut into the stone , a long cruel slice across the mountain side ,\n'
          'no light penetrates it shadowy depths\n')
    time.sleep(2)
    print('To your right is a well built entrance of white stone ,\n'
          'an arch protrudes from the mouth supported by elegant pillars of the same white stone \n'
          'The rock itself seems to be giving off a kind of light,beckoning  you\n')


def chooseCave():
    print("Would you like to examine the caves?")
    if input() == 'yes' or input() == 'y' or input() == 'Y' or input() == 'Yes':
        describeCaves()
    else:
        print('which cave will you venture down? (Right 1 or Left 2)')
    cave = ""
    while cave != '1' and cave != '2':
        print('which cave will you venture down? (Right 1 or Left 2)')
        cave = input()
        return cave


def checkCave(chooseCave):
    print('You approach the cave of your choice......')
    time.sleep(2)
    print('The cave is dark , you feel an intense heat on your face.....')
    time.sleep(2)
    print('You see a glimmer out of the corner of your eye, do you examine?\n')
    chestAnswer = ''
    while chestAnswer != '1' and chestAnswer != '2':
        print('yes or no (1 or 2)')
        chestAnswer = input()
    if chestAnswer == 1:
        print('you open the chest and see that is is locked but a long wide dust patch leads away from it to a book '
              'bound in chain')
        time.sleep(1)
        print('As you approach you hear a shrill voice in your ear ')
        time.sleep(1)
        print('	Night Fury.\n'
              'Speed: Unknown.\n'
              'Size: Unknown.\n'
              'The unholy offspring of lightning and death itself. '
              'Never engage this dragon. Your only chance:'
              ' Hide and pray it does not find you.')
    time.sleep(1)
    print('You walk for what seems like hours in the pitch black when suddenly you spot the beast across the cavern')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    if checkCave == str(friendlyCave):
        print('The dragon is immense,your eyes can barely see for its slow rhythmic breaths,\n'
              'its black injured wings curl around it to veil its eyes\n'
              'great gashes and scars are littered throughout its scales\n')
        time.sleep(1)


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    GameInrto()
    caveNumber = chooseCave()
    checkCave(caveNumber)
