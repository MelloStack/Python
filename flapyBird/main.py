import pygame
import os
import time

pygame.init()

running = True

screen = pygame.display.set_mode([500, 500])
player_mask = pygame.image.load("sprites/player.png")

player_mask_small = pygame.transform.scale(player_mask, (100, 100))
player_rect = player_mask_small.get_rect(midbottom = (100, 250))

pipe_up_mask = pygame.image.load("sprites/pipe_up.png")
pipe_up_mask_small = pygame.transform.scale(pipe_up_mask, (100, 100))
pipe_up_rect = pipe_up_mask_small.get_rect(midbottom = (500, 400))


pipe_down_mask = pygame.image.load("sprites/pipe_down.png")
pipe_down_mask_small = pygame.transform.scale(pipe_down_mask, (100, 100))
pipe_down_rect = pipe_down_mask_small.get_rect(midbottom = (350, 0))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(player_mask_small, player_rect)
    screen.blit(pipe_up_mask_small, pipe_up_rect.inflate(100, 100))
    screen.blit(pipe_down_mask_small, pipe_down_rect.inflate(-200, -200))

    pipe_down_rect.x -= 1
    pipe_up_rect.x -= 1


    if pipe_down_rect.x <= -200 & pipe_up_rect.x <= -200:
        pipe_up_rect.x = 500
        pipe_down_rect.x = 350


        

    mouse_click = pygame.mouse.get_pressed()


    player_rect.y += 0.5

    if mouse_click[0] == True:
        player_rect.y -= 3

    if pipe_down_rect.colliderect(player_rect) == True:
        main()
    if pipe_up_rect.colliderect(player_rect) == True:
        main()

    icon = pygame.image.load(os.path.join('sprites/player.png'))

    pygame.display.flip()
    pygame.display.set_caption("FlapyBird")
    pygame.display.set_icon(icon)

pygame.quit()