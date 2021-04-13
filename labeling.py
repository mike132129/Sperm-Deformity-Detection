# import pygame module in this program
import pygame
import glob, os, sys
from pygame.locals import FULLSCREEN, HWSURFACE
import pdb
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
clock = pygame.time.Clock()
  
# define the RGB value
# for white colour
white = (255, 255, 255)
  
# assigning values to X and Y variable
X = 600
Y = 700
  
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
  
# set the pygame window name
pygame.display.set_caption('Image')
  
# create a surface object, image is drawn on it.
image = glob.glob('./image/*')
crash = False

t = 0
category = 0

# infinite loop
while not crash:
  
    # completely fill the surface object
    # with white colour
    display_surface.fill(white)
  
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    img = pygame.image.load(image[t])
    display_surface.blit(pygame.transform.scale(img, (600, 600)), (0, 0))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
  
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :
  
            # deactivates the pygame library
            pygame.quit()
  
            # quit the program.
            crash = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print('labeling finished')
                t += 1
                pygame.display.update()

            elif event.key == pygame.K_c:
                print('labeling continue')
                pygame.display.update() 

            elif event.key == pygame.K_RETURN:
                print('start labeling')
                pygame.display.update()

            elif event.key == pygame.K_s:
                print('label save', category, left/X, top/X, (right-left)/X, (bottom-top)/X)
                file_name = image[t].split('/')[-1].split('.')[0]
                f = open('./label/' + file_name + '.txt', 'a')
                f.write(str(category) + ' ' + str(left/X) + ' ' + str(top/X) + ' ' + str((right-left)/X) + ' ' + str((bottom-top)/X) + '\n')
                f.close()
                pygame.display.update() 

            elif event.key == pygame.K_n:
                category = 0

            elif event.key == pygame.K_a:
                category = 1

            elif event.key == pygame.K_ESCAPE:
                crash = True


        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, top = pygame.mouse.get_pos()
            print('button down')

        elif event.type == pygame.MOUSEBUTTONUP:
            right, bottom = pygame.mouse.get_pos()
            pygame.draw.rect(display_surface, (255, 0, 0), (left, top, right-left, bottom-top), width=5)
            print('button up', left, top, right, bottom)
            # Draws the surface object to the screen.  
            pygame.display.update()

        clock.tick(1000)