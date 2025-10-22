import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

curr_state = "WAITING" #originally state will be obviously be waiting
cd_start = 0
r_start = 0
g_start = 0

while running:

    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # print("Spacebar clicked")
                if curr_state=="WAITING":
                    
                    curr_state="COUNTDOWN"
                    cd_start = pygame.time.get_ticks()

                if curr_state == "GREEN":
                    
                    react_time = pygame.time.get_ticks() - g_start
                    print("Reaction time:", react_time, "ms")
                    curr_state = "FINISHED"

        if event.type == pygame.QUIT:
            running = False

    if curr_state == "COUNTDOWN":
        if pygame.time.get_ticks() - cd_start >= 3000:
            curr_state = "READY"
            r_start = pygame.time.get_ticks()
            t = random.randrange(2000,10000)

    if curr_state == "READY":
        if pygame.time.get_ticks() - r_start >= t:
            curr_state = "GREEN"
            g_start = pygame.time.get_ticks()

    if curr_state in ["WAITING","COUNTDOWN","READY","FINISHED"]:
        screen.fill("red")
    elif curr_state == "GREEN":
        screen.fill("green")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()