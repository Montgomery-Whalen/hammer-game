# Import libraries
import pygame
import math

# initialize game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keyPresses = 0
startTime = None
clock = pygame.time.Clock()
timer = 0
inGame = True

# load images

# Game is running
while inGame:
   # clear screen before drawing it again
   screen.fill(0)
   # draw elements
   
   # update the screen
   pygame.display.flip()
   # loop through the events
   for event in pygame.event.get():
      # check if event is X button
      if event.type == pygame.QUIT:
         pygame.quit()
         exit(0)
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            if startTime:
               timer = pygame.time.get_ticks() - startTime
               if timer < 5000:
                  keyPresses = keyPresses + 1
               else:
                  inGame = False
            if startTime is None:
               startTime = pygame.time.get_ticks()
               keyPresses = keyPresses + 1
            print(keyPresses)
print("you did " + str(keyPresses) + " many")