#Source: https://stackoverflow.com/questions/56410741/typeerror-bool-object-is-not-callable-in-pygame
import pygame
import time
pygame.init()


pygame.display.set_caption('Platformer')
class Game:
    def __init__(self):
        self.x=7
        self.y=400
        self.width=40
        self.height=60
        self.vel=7
        self.run=True
        self.isJump=False
        self.jumpCount=10
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.flag = False
        self.win=pygame.display.set_mode((1200, 600))
    #def playerCollide():
    def GameLoop(self):
        while run:
            print(y)
            if self.flag == False:
                print('yes')

            pygame.time.delay(15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    self.run == False
            keys = pygame.key.get_pressed()

            if self.flag == False and keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                self.starttime = pygame.time.get_ticks()
                self.flag = True
                self.isJump=True
            if self.flag == True and pygame.time.get_ticks() - starttime >= 475:
                self.flag = False

            if keys[pygame.K_LEFT] and self.x > self.vel:
                self.x-=self.vel
            if keys[pygame.K_RIGHT] and self.x < 1200 - self.width - self.vel :
                self.x+=self.vel
            if not(self.isJump):
                if keys[pygame.K_DOWN] and self.y < 600 - self.height - self.vel:
                    self.y += 0

            else:
                if self.jumpCount >= -10:
                    self.y -= (self.jumpCount * abs(self.jumpCount)) * .55
                    self.jumpCount -= 1
                else:
                    self.jumpCount = 10
                    self.isJump = False
            self.win.fill((255,255,255))
            pygame.draw.rect(self.win, (0, 0, 0), (self.x,y, self.width, self.height))
            pygame.display.update()

g=Game()
g.run()