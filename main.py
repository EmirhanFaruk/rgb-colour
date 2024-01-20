
# Modification date: Sat Oct  8 10:37:52 2022

# Production date: Sun Sep  3 15:44:13 2023

import pygame
import random

h = 500
w = 700
"""
w, h = pygame.display.get_surface().get_size()
w = w // 2
h = h // 2
"""
#pygame.display.set_mode((0,0),pygame.FULLSCREEN)
win = pygame.display.set_mode((w,h))
pygame.init()


clock = pygame.time.Clock()

def draw_line():
    pygame.draw.line(win, give_colour(), (random.randint(0,w),random.randint(0,h)), (random.randint(0,w),random.randint(0,h)))

#colour = (255, 255, 255)
def give_colour():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))



#130-230

def draw_colour_line(colour):
    colours = ["r", "g", "b"]
    rgbs = [(255, 0, 255), (0, 255, 0), (0, 0, 255)]
    for i in range(len(colours)):
        if colours[i] == colour:
            pygame.draw.line(win, rgbs[i], (random.randint(0,w),random.randint(0,h)), (random.randint(0,w),random.randint(0,h)))



r, g, b, turn, going = 1, 1, 1, "r", "up"
def draw_colourful_line(c1, c2, r = 1, g = 1, b = 1, turn = "r", going = "up"):
    rgb_letter_list = ["r", "g", "b"]
    rgb_value_list = [r, g, b]
    for i in range(len(rgb_letter_list)):
        if turn == rgb_letter_list[i]:
            if rgb_value_list[i] == 255:
                going = "down"
            elif rgb_value_list[i] == 0:
                turn = rgb_letter_list[(i + 1) % 3]
                going = "up"
            if going == "up":
                rgb_value_list[i] += 1
            else:
                rgb_value_list[i] -= 1


    pygame.draw.line(win, (rgb_value_list[0], rgb_value_list[1], rgb_value_list[2]), c1, c2)
    return rgb_value_list[0], rgb_value_list[1], rgb_value_list[2], turn, going












r2, g2, b2, turn2,  going2 = 1, 1, 1, "r", "up"
def draw_colourful_rectangle(x1, y1, x2, y2, r = 1, g = 1, b = 1, turn = "r", going = "up"):
    rgb_letter_list = ["r", "g", "b"]
    rgb_value_list = [r, g, b]
    for i in range(len(rgb_letter_list)):
        if turn == rgb_letter_list[i]:
            if rgb_value_list[i] == 255:
                going = "down"
            elif rgb_value_list[i] == 0:
                turn = rgb_letter_list[(i + 1) % 3]
                going = "up"
            if going == "up":
                rgb_value_list[i] += 1
            else:
                rgb_value_list[i] -= 1
                if not rgb_value_list[(i + 1) % 3] + 2 > 255: 
                    rgb_value_list[(i + 1) % 3] += 2
    pygame.draw.rect(win, (rgb_value_list[0], rgb_value_list[1], rgb_value_list[2]), (x1, y1, x2, y2))
    return rgb_value_list[0], rgb_value_list[1], rgb_value_list[2], turn, going
            

running = True
while running:

    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()






    win.fill((0, 0, 0))
    #pygame.draw.line(win, give_colour(), (random.randint(0,w),random.randint(0,h)), (random.randint(0,w),random.randint(0,h)))
    r, g, b, turn, going = draw_colourful_line((w//5, h//5), (w//5 * 4, h//5 * 4), r, g, b, turn, going)
    r2, g2, b2, turn2, going2 = draw_colourful_rectangle(w//3, h//3, w//3, h//3, r2, g2, b2, turn2, going2)
    pygame.display.flip()
