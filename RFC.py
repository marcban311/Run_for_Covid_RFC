import pygame,sys, random 

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,904))
    screen.blit(floor_surface,(floor_x_pos +576,904))

def draw_bg():
    screen.blit(bg_surface,(bg_x_pos,0))
    screen.blit(bg_surface,(bg_x_pos+576,0))

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('object/tło.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
bg_x_pos= -1

floor_surface = pygame.image.load('object/podłoga.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

mario_surface = pygame.image.load('object/pic2.png').convert()
mario_surface = pygame.transform.scale2x(mario_surface)
mario_rect = mario_surface.get_rect(center = (100,512))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    bg_x_pos -=0.5
    draw_bg()
    floor_x_pos -=1
    draw_floor()

    if bg_x_pos<= -576:
        bg_x_pos = 0

    if floor_x_pos<= -576:
        floor_x_pos = 0

    screen.blit(mario_surface,mario_rect)
    pygame.display.update()
    clock.tick(120)