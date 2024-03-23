#Source: https://stackoverflow.com/questions/62030196/typeerror-argument-1-must-be-pygame-surface-not-str-after-window-blit
import pygame # importing module
pygame.init() # initiates pygame
window = pygame.display.set_mode((500,500)) # creates a 500x500px window
pygame.display.set_caption("PYGAME TEST") # sets caption, self explanatory

class player(object):
    def __init__(self,x,y,width,height,jH):
        self.x= x # x coordinate of the character
        self.y = y # y coordinate of the character
        self.w = width  # width of the character
        self.h = height # Height of the character
        self.v = 20 # Speed of the character
        self.jump = False # Will determine whether the character is jumping
        self.jumpC = jH # Jump variable
        self.direction = "left"
        self.isWalking = 0
    def redraw(self,wind):
        global number
        global previousnumber
        global selectedimage
        if previousnumber == number:
            selectedimage = walkUp[0]
        previousnumber = number

        window.blit(selectedimage,(self.x,self.y))

run = True # variable used in a loop, its true if the program is still running.
walkRight = [pygame.image.load('right1.png'), pygame.image.load('right2.png'), pygame.image.load('right3.png')]
walkLeft = [pygame.image.load('left1.png'), pygame.image.load('left2.png'), pygame.image.load('left3.png')]
walkUp = [pygame.image.load('front1.png').convert(), pygame.image.load('front2.png'), pygame.image.load('front3.png')]
walkDown = [pygame.image.load('back1.png'), pygame.image.load('back2.png'), pygame.image.load('back3.png')]
bg = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
number = 0
selectedimage = walkUp[number]
previousnumber = -2

def spriteupdate(d,a,man):
    global number
    if man.direction != d:
        man.direction  = d
        changed(0,a,man)
    else:
        number+= 1
        if number>2:
            number = 0
            changed(number,a)
        else:
            changed(number,a,troop)
def changed(numb, direction,man):
    global number
    global selectedimage
    number = numb
    selectedimage = man.direction[number]
def update(man):
    troop.redraw(window)
    window.blit(bg,(0,0))
    pygame.display.update()
troop = player(250,250,10,10,10)
while run:
    clock.tick(15)# FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if event quits, presses the x button
            run = False # breaks loop
        keys = pygame.key.get_pressed() # gets the keys pressed

    if keys[pygame.K_LEFT]:# pressed left arrow, x coordinate changes by - speed
        #direction, array
        spriteupdate("left",walkLeft,troop)
        if troop.x <= -10:
            pass
        else:
            troop.x-=troop.v
    if keys[pygame.K_RIGHT]: # similar here
        spriteupdate("right", walkRight,troop)
        if troop.x >= 470:
            pass
        else:
            troop.x+=troop.v

    if not(troop.jump): # Only works if the character isn't jumping
        if keys[pygame.K_SPACE]: # The character is jumping. changes variable.
            troop.jump = True
        if keys[pygame.K_UP]: # same here
            spriteupdate("down",walkDown,troop)
            if troop.y <= -10:
                pass
            else:
                troop.y-=troop.v
        if keys[pygame.K_DOWN]: # same here
            spriteupdate("up",walkUp,troop)
            if troop.y >= 470:
                pass
            else:
                troop.y+=troop.v
    else:
        if troop.jumpC >= -10: # jumpC is already bigger than -10, this is called
            num = 1 # number, will be set to -1 if jumpC becomes a negative number
            if troop.jumpC < 0: 
                num = -1 # there. 
            troop.y-= (troop.jumpC ** 2) * 0.5 * num # y subtracted (goes up) by the square of jumpC * half * num
            troop.jumpC -= 1 # Subtracts 1
        else:
            troop.jump = False # If Jump c is smaller than -10, jump has finished.
            troop.jumpC = 10 # reset variable

    update(troop)


pygame.quit()