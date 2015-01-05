import math, os, pygame
X_MAX = 800
Y_MAX = 600
STEP_SIZE = 4
class ShipSprite(pygame.sprite.Sprite):
    '''
    This is the user controlled space ship in Spaace
    '''
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([16,16])
        self.rect = self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]
        #store lives in main
        #bullet type can be stored here 
        self.bullet_type = 1
        self.image.fill((0,255,0))
        self.god = False
    def move(self, position):
        ''' moves to given position'''
        if position[0] + 16 > X_MAX:
            # The ship itself is 16 pixels long
            self.rect.x = X_MAX -16
        else:
            self.rect.x = position[0]
    def update(self):
        '''
        Empty function so that all sprite groups can be updated
        '''
        pass
class BulletSprite(pygame.sprite.Sprite):
    '''
    This is an instance of a bullet. 
    '''
    def __init__(self, position, owner, direc, speed, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8,16])
        self.rect = self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]
        self.owner = owner # -1 is player, 1 is enemy, controls y-direc
        self.direc = direc # is x-velocity
        self.speed = speed # >1 float multiplier to speed of enemies
        self.image.fill(color)
    def  update(self):
        '''
        moves the bullet every step
        '''
        self.rect.y += self.owner * STEP_SIZE * self.speed#moves up/down
        self.rect.x += self.direc
        #will delete the objects when they go off screen in main
class EnemySprite(pygame.sprite.Sprite):
    '''
    This is the enemy ships/meteors
    '''
    def __init__(self, position,fires, direction, color, score, length = 16, width = 16):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([length,width])
        self.rect = self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]
        self.fires = fires #boolean of whther it attacks
        self.direc = direction #x-velocity
        self.score = score
        self.image.fill(color)
        self.refactory = 999
        self.charge = 0
    def update(self):
        '''
        moves the enemies every step
        '''
        self.rect.y += STEP_SIZE
        self.rect.x += self.direc
        self. charge += 1
        if self.charge == self.refactory:
            return self.fire()
        else:
            return 0
        
    def fire(self):
        return 0
    #need to find some way to make more interesting attack patterns
class Alien1Sprite(EnemySprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.rect = self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]
        self.fires = True #boolean of whther it attacks
        self.direc = 0 #x-velocity
        self.score = 30
        self.image.fill((148,0,211))
        self.refactory = 10
        self.charge = 0 
    def fire(self):
        # self.charge = 0
        bullet = BulletSprite((self.rect.x+4,self.rect.y),1,0,2,(255,0,0))
        return bullet


class CrateSprite(pygame.sprite.Sprite):
    '''
    objects that grant powerups or score boosts
    '''
    def __init__(self, position, contains, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([16,16])
        self.rect = self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]
        self.image.fill(color)
        self.contains = contains #(score, bullet level, lives)
    def update(self):
        self.rect.y += 3*STEP_SIZE

# TODO
# make enemy class have reasonably different sizes and shapes
# make enemyies have different fire patterns
# consider inheritence? 
# make powerup crates fall

# make levels work nicely:
#     possibly by takign most of the main and making it a function of a level class 
#     save the levels to a file
# consider rewrite ith heath?