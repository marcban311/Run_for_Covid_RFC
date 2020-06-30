import pygame, sys, random 

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,904))
    screen.blit(floor_surface,(floor_x_pos +576,904))

def draw_bg():
    screen.blit(bg_surface,(bg_x_pos,0))
    screen.blit(bg_surface,(bg_x_pos+576,0))

def create_virus():
    random_virus_pos = random.choice(virus_random_list)
    new_virus = virus_surface.get_rect(center = (600, random_virus_pos))
    return new_virus

def move_virus(viruses):
    for virus in viruses:
        virus.centerx -= 5
    return viruses

def draw_virus(viruses):
    for virus in viruses:
        screen.blit(virus_surface,virus)

def check_collision(viruses):
    colision= 0
    for virus in viruses:
        if mario_rect.colliderect(virus):
            return False    
    return True

def mario_animation():
    new_mario= mario_frames[mario_index]
    new_mario_rect = new_mario.get_rect(center=(100, mario_rect.centery))
    return new_mario, new_mario_rect

def score_display(game_state):
    score_surface = game_font.render(str(int(score)),True,(255, 255, 255))
    score_rect = score_surface.get_rect(center = (288,100))
    screen.blit(score_surface,score_rect)

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('Bo.tTF', 100)
#const
gravity = 0.4
mario_movement = 0
game_activ = True
mario_minimum_y = 861
score= 0
high_score= 0 

#import grafik
bg_surface = pygame.image.load('object/tło.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
bg_x_pos= 0
floor_surface = pygame.image.load('object/podłoga.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

virus_surface = pygame.image.load('object/corona.png').convert_alpha()

mario1_surface = pygame.image.load('object/pic2aaaa.png').convert_alpha()
mario1_surface = pygame.transform.scale2x(mario1_surface)

mario2_surface = pygame.image.load('object/pic2aa.png').convert_alpha()
mario2_surface = pygame.transform.scale2x(mario2_surface)

mario3_surface = pygame.image.load('object/pic2aaa.png').convert_alpha()
mario3_surface = pygame.transform.scale2x(mario3_surface)

mario_frames = [mario1_surface,mario2_surface,mario3_surface]
mario_index = 0 

mario_surface= mario_frames[mario_index]
mario_rect = mario_surface.get_rect(center = (100, mario_minimum_y))

MARIOSTEP = pygame.USEREVENT + 1
pygame.time.set_timer(MARIOSTEP,50)


bat_surface = pygame.image.load('object/bat.png').convert_alpha()
bat_surface = pygame.transform.scale2x(bat_surface)

virus_random_list= [850, 860, 800, 830, 810, 790, 780, 870, 750]
virus_y_pos_list = []

SPAWNVIRUS = pygame.USEREVENT
pygame.time.set_timer(SPAWNVIRUS,1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE and game_activ:
                mario_movement = 0
                mario_movement -=12
            if event.key== pygame.K_SPACE and game_activ == False:
                game_activ= True
                virus_y_pos_list.clear()
                mario_rect.center = (100, mario_minimum_y)
                score = 0
        
        if event.type == SPAWNVIRUS:
            virus_y_pos_list.append(create_virus())

        if event.type == MARIOSTEP:
            if mario_index <2:
                mario_index +=1
            else:
                mario_index = 0

            mario_surface, mario_rect = mario_animation()
    
    bg_x_pos -= 0.5
    draw_bg()
    floor_x_pos -= 5
    draw_floor()

    if game_activ:
    # mario i grawitacja
        mario_movement += gravity 
        mario_rect.centery += mario_movement
        screen.blit(mario_surface,mario_rect)
        game_activ = check_collision(virus_y_pos_list)
        if mario_rect.centery >= mario_minimum_y:
            mario_movement= 0
        score_display()
    #virus
        virus_y_pos_list = move_virus(virus_y_pos_list)
        draw_virus(virus_y_pos_list)

    #kolizja
        check_collision(virus_y_pos_list)
        score += 0.01
#zapętlenie tła 
    if bg_x_pos<= -576:
        bg_x_pos = 0

    if floor_x_pos<= -576:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)