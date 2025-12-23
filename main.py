#BRANCH ONE
#
#
import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,600))
    screen.blit(floor_surface,(floor_x_pos + 576,600))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos -100))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 720:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe, pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
           return False
           
    if bird_rect.top <= -100 or bird_rect.bottom >= 600:
        return False
    
    return True
        
pygame.init()
screen = pygame.display.set_mode((576,720))
clock = pygame.time.Clock()

#Game varibales
gravity = 0.25
bird_movement = 0
game_active = True

bg_surface = pygame.image.load('sprites/background-night.png')
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (140,340))

pipe_surface = pygame.image.load('sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [200, 300, 400,]


while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 9
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (140,340)
            
       if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            print(pipe_list)
                 
         
          
    screen.blit(bg_surface, (0,-250))
    if game_active:
    #BIRD
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)
        game_active = check_collision(pipe_list)
    #Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
    #Floor
    floor_x_pos -= 1
    draw_floor()
    
    if floor_x_pos <= -576:
        floor_x_pos = 0
    
    
    pygame.display.update()
    clock.tick(60)