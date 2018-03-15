# Import libraries
import pygame
import math
import random

def randomColor():
    return tuple(random.randint(0,255) for i in range(3))

class SwingingHammer:
   def __init__(self, size, swingDegrees, frames):
      self.swingAngle = swingDegrees
      self.swingSteps = frames
      self.step = 0
      self.surface = pygame.Surface(size)
      ckey = (255,0,255)
      self.surface.fill(ckey)
      self.surface.set_colorkey(ckey)
      w, h = size
      headW, headH = w, .25*h
      handleW, handleH = .05*w, h - headH
      centerX = w/2
      headRect = (0, 0, headW, headH)
      handleRect = (centerX - .5*handleW, headH, handleW, handleH)
      headfill = (200, 200, 200)
      handlefill = randomColor()
      pygame.draw.rect(self.surface, headfill, headRect)
      pygame.draw.rect(self.surface, handlefill, handleRect)

   def draw(self, targSurf, bottomHandlePoint):
      rot = self.step * (self.swingAngle / self.swingSteps)
      rotatedSurf = pygame.transform.rotate(self.surface, rot)
      targSurf.blit(rotatedSurf, bottomHandlePoint)
      
   def stepAnimation(self):
      self.step += 1

def main(): 
   # initialize game
   pygame.init()
   width, height = 640, 480
   screen=pygame.display.set_mode((width, height))
   keyPresses = 0
   bgColor = (255,255,255)
   clock = pygame.time.Clock()
   timeLimit = 10000
   targHits = 10
   inGame = True
   timeOver = False
   startTicks = None
   hammerSize = (70, 200)
   hammerPos = (width // 2, height // 2)
   
   pygame.display.update()
   #Game is running
   while inGame:
      if startTicks is None:
         startTicks = pygame.time.get_ticks()

      # clear screen before drawing it again
      screen.fill(bgColor)

      if not timeOver:
         nowTicks = pygame.time.get_ticks()
         elapsed = nowTicks - startTicks
         timeOver = elapsed > timeLimit
         if timeOver:
            print("Ran out of time")
         # draw text that says mash spacebar
      else:
         # draw animation, 90 degree swing, 20 frames
         frames = 20
         hammer = SwingingHammer(hammerSize, 90, frames)
         for i in range(20):
            screen.fill(bgColor)
            hammer.stepAnimation()
            hammer.draw(screen, hammerPos)
            pygame.time.delay(50)
            pygame.display.update()
         # listen to television
         # my bloody valentine
      
      # draw elements
      
      # update the screen
      # loop through the events
      for event in pygame.event.get():
         # check if event is X button
         if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               if not timeOver:
                  keyPresses = keyPresses + 1
                  if keyPresses == targHits:
                     print("YOU DID IT")
                     timeOver = True
                  print(keyPresses)
                  
   print("you did " + str(keyPresses) + " many")

if __name__ == "__main__":
   main()
