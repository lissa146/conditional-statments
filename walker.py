import pygame
import random
pygame.init()#initializes Pygame
pygame.display.set_caption("random walk")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
xpos = 400 #start point for x
ypos = 400 #start point for y
xdir = 1
ydir = 1
color = (100, 100, 200)
change = 1
list = [  ]


#render section---------------------------------------------
    
for i in range(10000): #loop a bunch of times
    Roll = random.randrange(1, 100) #change x direction if you generate a 1 
    
    
    if Roll == 1:
        change = random.randrange(1, 5)
    if change == 1:
        xpos += xdir
    elif change == 2:
        xpos -= xdir
    elif change == 3:
        ypos += ydir
    elif change == 4:
        ypos -= ydir
    

    
    
    #if yRoll == 1:
       # ydir*=-1
        #ypos += ydir
   # else:
      #  ypos += ydir
        
    
        
    #start back in the middle if you go off the screen
    if xpos > 800 or xpos <0:
        xpos = 400
        color = (random.randrange(255), random.randrange(255), random.randrange(255))
    if ypos > 800 or ypos< 0:
        ypos = 400
        color = (random.randrange(255), random.randrange(255), random.randrange(255))

    pygame.draw.ellipse(screen, (color), (xpos,ypos, 8, 8))

    pygame.display.flip()


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break

#end game loop##############################################
pygame.quit()
