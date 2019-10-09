import pygame
import sys
import random
import time
from pygame.locals import *
from spaceship import *
from alien import *
from miscVariables import *
from background import *
from miscFunctions import *

pygame.init()
pygame.font.init()

myFont = pygame.font.Font(None, 40)


all_sprites_list = pygame.sprite.Group()
# print type (all_sprites_list)

mainDisplay = pygame.display.set_mode((WindowWidth, WindowHeight))
# pygame.draw.line (mainDisplay, BLACK, (100, 100), (400, 400), 2)

background = Background(
    'simple-star-space-background-effect-footage-023768280_prevstill.jpeg', [0, 0])

# spaceship.makeSmallMissile()

# t = alien.returnRandomAlienPosition() # AlienPosition()
# alien = alienClass (0, 0)
# alien.rect.x = t[0] + 10
# alien.rect.y = t[1] + 10

# all_sprites_list.add (spaceship.makeSmallMissile())

gameFPSClock = pygame.time.Clock()

aliens = pygame.sprite.Group()
smallMissiles = pygame.sprite.Group()
bigMissiles = pygame.sprite.Group()

scoreText = myFont.render("Score : ", False, WHITE)

all_sprites_list.add(spaceship)

while True:
    # m = spaceship.makeSmallMissile()
    mainDisplay.fill(BLACK)
    mainDisplay.blit(background.image, background.rect)

    mainDisplay.blit(scoreText, (320, 914))
    actualScore = myFont.render(str(score), False, WHITE)
    mainDisplay.blit(actualScore, (440, 914))
    # mainDisplay.blit(mainDisplay, 'lonelyspace.png', [0,0])

    # for i in range (0, 9):
    pygame.draw.line(mainDisplay, WHITE, (0, 100 * 9 + 5),
                     (900, 100 * 9 + 5), 2)

    # for i in range (0, 9):
    # 	pygame.draw.line (mainDisplay, YELLOW, (100 * i, 0), (100 * i, 900), 4)

    for i in pygame.event.get():
        if i.type == QUIT:
            # print "Score is ", score
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                # print "Score is ", score
                pygame.quit()
                breakFlag = 1
                break
                # sys.quit()
        elif i.type == pygame.KEYUP:
            # if i.key == pygame.K_a:
            # 	spaceship.moveLeft (2)
            # elif i.key == pygame.K_d:
            # 	spaceship.moveRight (2)
            if i.key == pygame.K_SPACE:
                m = spaceship.makeSmallMissile()
                smallMissiles.add(m)
                # all_sprites_list.add (m)
            elif i.key == pygame.K_s:
                n = spaceship.makeBigMissile()
                bigMissiles.add(n)
                # all_sprites_list.add (n)
            else:
                pass

    if breakFlag == 1:
        break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        spaceship.moveLeft(3)
    if keys[pygame.K_d]:
        spaceship.moveRight(3)
    # if keys[pygame.K_SPACE]:
    # 	m = spaceship.makeSmallMissile()
    # 	smallMissiles.add (m)
    # 	# all_sprites_list.add (m)
    # if keys[pygame.K_s]:
    # 	n = spaceship.makeBigMissile()
    # 	bigMissiles.add (n)
        # all_sprites_list.add (n)

    # print m
    # while tempCount < 20:
    # 	print "hello"
    # 	for i in range(0, len(smallMissiles)):
    # 		smallMissiles[i].moveUp()
    # 	tempCount+=1
    # 	if (tempCount == 20):
    # 		tempCount = 0

    # if alienCount % 10 == 0:
    # 	for i in range(0, len(smallMissiles)):
    # 		smallMissiles[i].moveUp()

    if alienCount % 800 == 0:
        aliens.add(makeAlien())

    if alienCount % 1 == 0:
        for i in bigMissiles:
            i.moveUp(3)

    if alienCount % 100 == 0:
        for i in aliens:
            i.reduceLifetime()
            if i.returnLifetime() <= 0:
                aliens.remove(i)

    if alienCount % 1 == 0:
        for i in smallMissiles:
            i.moveUp(3)
        # for i in range(0, len(bigMissiles)):
        # 	bigMissiles[i].moveUp()

    for i in smallMissiles:
        if i.rect.y < 0:
            smallMissiles.remove(i)
            # print "removed small missile"

    for i in bigMissiles:
        if i.rect.y < 0:
            bigMissiles.remove(i)
            # print "removed big missile"

    for i in smallMissiles:
        alienCollisionList = pygame.sprite.spritecollide(i, aliens, False)
        for alien in alienCollisionList:
            # print ("Oh Fuck! collision")
            aliens.remove(alien)
            # alien.newColor (PINK)
            # aliens.draw (mainDisplay)
            score += 1
            # break
            smallMissiles.remove(i)
            # print "Removed missile hopefully"

    for i in bigMissiles:
        CollisionList = pygame.sprite.spritecollide(i, aliens, False)
        for alien in CollisionList:
            # print ("Oh Fuck. Minor collision")
            bigMissiles.remove(i)
            alien.increaseLifetime()
            # print "lifetime of alien is now", alien.returnLifetime()
            alien.gotHitByBigMissile()
            # oldLifetime = alien.returnLifetime()
            # oldLocation = alien.returnLocation()
            # aliens.remove(alien)
            # newAlien = alienClass (0, 0, oldLocation, oldLifetime+5)
            # aliens.add (newAlien)
            # newAlien =
            aliens.update()
            aliens.draw(mainDisplay)
            # aliens.remove (alien)
            # bigMissiles.remove(i)
            # alien.newColor (ORANGE)
            # aliens.add (alien)
            # aliens.draw (mainDisplay)
            break

    all_sprites_list.update()
    smallMissiles.update()
    bigMissiles.update()
    aliens.update()

    all_sprites_list.draw(mainDisplay)
    smallMissiles.draw(mainDisplay)
    bigMissiles.draw(mainDisplay)
    aliens.draw(mainDisplay)

    alienCount += 1
    # print "time is now : ", alienCount

    pygame.display.update()
    gameFPSClock.tick(100)
