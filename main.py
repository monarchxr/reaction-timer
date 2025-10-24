import pygame
import random

pygame.init()
pygame.display.set_caption("Reaction Timer")
text_font = pygame.font.SysFont("Arial", 30)
screen = pygame.display.set_mode((1280,720))
X = 465
Y = 100

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

clock = pygame.time.Clock()
running = True

curr_state = "WAITING" #originally state will be obviously be waiting
cd_start = 0
r_start = 0
g_start = 0
react_time = 0

while running:

    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # print("Spacebar clicked")
                if curr_state == "WAITING":
                    print("Starting test in 3 seconds. Good Luck!")
                    curr_state="COUNTDOWN"
                    cd_start = pygame.time.get_ticks()

                elif curr_state == "READY" or curr_state == "COUNTDOWN":
                    print("User clicked too early")
                    curr_state = "EARLY"

                elif curr_state == "EARLY":
                    print("Restarting test")
                    curr_state = "WAITING"

                elif curr_state == "GREEN":
                    react_time = pygame.time.get_ticks() - g_start
                    print("Reaction time:", react_time, "ms")
                    print("Press spacebar to reset and start new test")
                    curr_state = "FINISHED"

                elif curr_state == "FINISHED":
                    print("Test finished, resetting")
                    curr_state = "WAITING"

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

    if curr_state in ["COUNTDOWN","READY"]:
        screen.fill((180,50,50))
    elif curr_state in ["WAITING","FINISHED", "EARLY"]:
        screen.fill((240,240,240))
    elif curr_state == "GREEN":
        screen.fill((50,205,50))

    if curr_state == "WAITING":
        draw_text("Welcome to Reaction Timer!", text_font, (0,0,0), X+15, Y)
        draw_text("Press spacebar to start the test. It will begin in 3 seconds.", text_font, (0,0,0), X-130,Y+200)

    if curr_state == "COUNTDOWN":
        draw_text("Wait for the green screen to show!", text_font, (0,0,0), X-20,Y+100)
        draw_text("Press the spacebar when it appears", text_font, (0,0,0), X-20,Y+200)

    if curr_state == "EARLY":
        draw_text("You pressed too early! Press spacebar to restart", text_font, (0,0,0), X-75,Y+100)

    if curr_state == "FINISHED":
        draw_text("Test completed successfully!", text_font, (0,0,0), X+20,Y+100)
        draw_text(f"Your reaction time is : {react_time} ms", text_font, (0,0,0), X+20, Y+200)
        draw_text("Press the spacebar to go again!", text_font, (0,0,0), X+6, Y+450)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()