#Source: https://stackoverflow.com/questions/56959631/im-getting-a-nameerror-from-using-the-event-function-from-pygame
#Drawing Rectangles (later used as buttons)
batteryBtn = pygame.draw.rect(display, red, (0,0,100,50))
bulbBtn = pygame.draw.rect(display, green, (100,0,100,50))
resistorBtn = pygame.draw.rect(display, blue, (200,0,100,50))

#Initialising the images
img1 = pygame.image.load(r'C:\Users\Amine\Pictures\Battery.jpg')
img2 = pygame.image.load(r'C:\Users\Amine\Pictures\bulbOn.jpg')
img3 = pygame.image.load(r'C:\Users\Amine\Pictures\bulbOff.jpg')
img4 = pygame.image.load(r'C:\Users\Amine\Pictures\Resistor.jpg')

if event.type == pygame.MOUSEBUTTONDOWN:
    if event.button == 1:
        if batteryBtn.collidepoint(pos):
            display.blit(img1, (0, 100))