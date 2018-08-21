import pygame
from pygame.locals import *
from random import *
import time

from spaceship import Spaceship
from alien import *
from missile import *


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

score = [0]
timestamp = 0

def main():
    pygame.init()

    pygame.display.set_caption("Space Invaders")

    screen = pygame.display.set_mode((800,860))
    pygame.draw.line(screen, WHITE, [0, 800], [800, 800], 1)

    all_sprites_list = pygame.sprite.Group()

    alien_list = pygame.sprite.Group()
    destroy_list = pygame.sprite.Group()
    poison_list = pygame.sprite.Group()


    main_spaceship = Spaceship(400,700)
    all_sprites_list.add(main_spaceship)
   

    clock = pygame.time.Clock()

    def displayScore():
        font = pygame.font.Font(None, 40)
        text1 = font.render("SCORE: " + str(score[0]), 1, WHITE)
        screen.blit(text1, (10, 820))

    running = True

    while running:

        pygame.display.flip()

        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [0, 800], [800, 800], 2)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    running = False

                elif event.key == pygame.K_d:
                    main_spaceship.moveRight(100)

                elif event.key == pygame.K_a:
                    main_spaceship.moveLeft(100)

                elif event.key == pygame.K_SPACE:
                    main_missile_destroy = MissileA(main_spaceship.getX())
                    destroy_list.add(main_missile_destroy)
                    all_sprites_list.add(main_missile_destroy)
                    main_missile_destroy.moveUp()

                elif event.key == pygame.K_s:
                    main_missile_poison = MissileB(main_spaceship.getX())
                    poison_list.add(main_missile_poison)
                    all_sprites_list.add(main_missile_poison)
                    main_missile_poison.moveUp()


        row = randint(0, 7)
        column = randint(0, 1)


        def spawnAlien():
            global timestamp
            if time.time() - timestamp >= 10:
                timestamp = time.time()
                main_alien = Alien(row, column)
                alien_list.add(main_alien)
                all_sprites_list.add(main_alien)


        for al in alien_list:
            al.draw(screen) 
            al.annihilate()

        for mis in destroy_list:
            mis.draw(screen)
            hit = pygame.sprite.spritecollide(mis, alien_list, True)
            if hit:
                mis.burnUp()
                score[0] += 1
                #increase score whenever an alien dies of direct consequence of being hit by a missile, i.e.shot down

            mis.moveUp()

        for mis in poison_list:
            mis.draw(screen)
            for al in alien_list:
                hit = mis.isCollide(al)

                if hit:
            
                    x = al.getX()
                    y = al.getY()
                    al.kill()
                    main_frozen_alien = frozenAlien(x, y) 
                    mis.burnUp()
                    alien_list.add(main_frozen_alien)
                    all_sprites_list.add(main_frozen_alien)

            mis.moveUp()


        main_spaceship.draw(screen)

        all_sprites_list.draw(screen)

        spawnAlien()

        displayScore()
        clock.tick(20)

if __name__ == "__main__":

    main()

pygame.quit()
quit()