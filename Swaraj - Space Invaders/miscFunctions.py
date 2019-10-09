import random
from alien import *


def returnRandomAlienPosition():
    x = random.randint(0, 7) * 100
    y = random.randint(0, 1) * 100
    return (x, y)


def makeAlien():
    t = returnRandomAlienPosition()  # AlienPosition()
    alien = alienClass(0, 0, t)
    # t = alien.returnRandomAlienPosition() # AlienPosition()
    # alien.rect.x = t[0] + 10
    # alien.rect.y = t[1] + 10
    return alien
