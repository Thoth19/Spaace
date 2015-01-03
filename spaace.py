import math, os, pygame, random
from classes import *
#initialize

pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

lives = 3
level = 1
stage = 1 #might not use these, but oh well
score = 0

bullet_group=pygame.sprite.Group()
enemy_group=pygame.sprite.Group()
all_group=pygame.sprite.Group()

while lives > 0:

    player = ShipSprite((X_MAX / 2, Y_MAX - 32))
    all_group.add(player)
    alive = True

    while alive:
        #need to figure out a way of encoding when enemies appear and where
        clock.tick(30)
        screen.fill((0,0,0))
        all_group.update()

        for event in pygame.event.get():
            if event.type != pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                player.move(mouse_pos)
        pressed = pygame.key.get_pressed()
        if pygame.K_SPACE in pressed:
            bullet = BulletSprite((player.rect.x,player.rect.y),-1,0,1,(0,0,255))
            #blue bullets
            all_group.add(bullet)
            bullet_group.add(bullet)

        for bullet in bullet_group:
            if X_MAX > bullet.rect.x < 0:
                bullet_group.remove(bullet)
                all_group.remove(bullet)
            if Y_MAX > bullet_group.rect.y < 0:
                bullet_group.remove(bullet)
                all_group.remove(bullet)
            #bullets must be on screen
            if bullet.owner == -1: #owned by player
                for enemy in enemy_group:
                    if bullet.rect.colliderect(enemy):
                        enemy_group.remove(enemy)
                        all_group.remove(enemy)
                    
        for danger in all_group:
            if not(danger == player):
                if danger.rect.colliderect(player.rect):
                    alive = False
                    lives -= 1
            else:
                # collisions with self don't matter
                pass