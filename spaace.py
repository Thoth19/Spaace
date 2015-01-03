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

pygame.display.set_caption('Spaace: Level %d, Stage %d, Lives %d, Score %d' % (level, stage, lives, score))

bullet_group=pygame.sprite.Group()
enemy_group=pygame.sprite.Group()
all_group=pygame.sprite.Group()

while lives > 0:

    player = ShipSprite((X_MAX / 2, Y_MAX - 32))
    all_group.add(player)
    alive = True
    level_counter = 0 # counter in array for enemies
    level_array = []
    for i in range(600):
        temp = []
        for j in range(50): #x distance across
            if i%10 == 0 and j%5 == 0:
                temp.append(1)
            elif i % 28 ==0 and j % 10 ==0:
                temp.append(2)
            else:
                temp.append(0)
        level_array.append(temp)

    #possibly make levels into objects?
    while alive and level_counter < len(level_array):
        #need to figure out a way of encoding when enemies appear and where
        for i in range(len(level_array[level_counter])):
            if level_array[level_counter][i] == 1:
                enemy = EnemySprite((i*16,0),False, 0, (139,69,19), 10)
                enemy_group.add(enemy)
                all_group.add(enemy)
            if level_array[level_counter][i] == 2:
                enemy = EnemySprite((i*16,0),True, 0, (148,0,211), 30)
                enemy_group.add(enemy)
                all_group.add(enemy)

        clock.tick(20)
        screen.fill((0,0,0))
        all_group.update()

        for event in pygame.event.get():
            if event.type != pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                player.move(mouse_pos)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            bullet = BulletSprite((player.rect.x + 4,player.rect.y - 16),-1,0,2,(0,0,255))
            #blue bullets
            all_group.add(bullet)
            bullet_group.add(bullet)
        if pressed[pygame.K_q]:
            pygame.display.quit()
            break

        for enemy in enemy_group:
            if enemy.fires and random.randint(1,50)==10:
                bullet = BulletSprite((enemy.rect.x,enemy.rect.y),1,0,2,(255,0,0))
                bullet_group.add(bullet)
                all_group.add(bullet)

        for bullet in bullet_group:
            if X_MAX > bullet.rect.x < 0:
                bullet_group.remove(bullet)
                all_group.remove(bullet)
            if Y_MAX > bullet.rect.y < 0:
                bullet_group.remove(bullet)
                all_group.remove(bullet)
            #bullets must be on screen
            if bullet.owner == -1: #owned by player
                for enemy in enemy_group:
                    if bullet.rect.colliderect(enemy):
                        score += enemy.score
                        enemy_group.remove(enemy)
                        all_group.remove(enemy)
                    
        for danger in all_group:
            if alive and not(danger == player):
                if danger.rect.colliderect(player.rect):
                    all_group.remove(player)
                    alive = False
                    lives -= 1
                    
            else:
                # collisions with self don't matter
                pass
        level_counter += 1
        pygame.display.set_caption('Spaace: Level %d, Stage %d, Lives %d, Score %d' %(level, stage,lives, score))
        all_group.draw(screen)
        pygame.display.flip()