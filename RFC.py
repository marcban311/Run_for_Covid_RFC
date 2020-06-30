import pygame, sys, random 

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,904))
    screen.blit(floor_surface,(floor_x_pos +576,904))

def draw_bg():
    screen.blit(bg_surface,(bg_x_pos,0))
    screen.blit(bg_surface,(bg_x_pos+576,0))

def create_virus():
    new_virus = virus_surface.get_rect(center = (288, 850))
    return new_virus

def move_virus(viruses):
    for virus in viruses:
        virus.centerx -= 5 
    return viruses

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

gravity = 0.25
mario_movement = 0

bg_surface = pygame.image.load('object/tło.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
bg_x_pos= 0

floor_surface = pygame.image.load('object/podłoga.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0
mario_minimum_y = 861

mario_surface = pygame.image.load('object/pic2.png').convert_alpha()
mario_surface = pygame.transform.scale2x(mario_surface)
mario_rect = mario_surface.get_rect(center = (100, mario_minimum_y))

virus_surface = pygame.image.load('object/corona.png').convert_alpha()
virus_surface = pygame.transform.scale2x(virus_surface)

bat_surface = pygame.image.load('object/bat.png').convert_alpha()
bat_surface = pygame.transform.scale2x(bat_surface)

virus_y_pos_list = []
SPAWNVIRUS = pygame.USEREVENT
pygame.time.set_timer(SPAWNVIRUS,1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                mario_movement = 0
                mario_movement -=12
        
        if event.type == SPAWNVIRUS:
            virus_y_pos_list.append(create_virus())


    bg_x_pos -= 0.5
    draw_bg()
    floor_x_pos -= 1
    draw_floor()

# mario i grawitacja
    mario_movement += gravity 
    mario_rect.centery += mario_movement
    screen.blit(mario_surface,mario_rect)
 if mario_rect.centery >= mario_minimum_y:
        mario_movement= 0
#virus



   
#zapętlenie tła 
    if bg_x_pos<= -576:
        bg_x_pos = 0

    if floor_x_pos<= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)