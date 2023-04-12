import pygame
import os
pygame.init()

screen = pygame.display.set_mode((1200, 500))

running=[pygame.image.load(os.path.join('Assets/Dino','DinoRun1.png')),pygame.image.load(os.path.join('Assets/Dino','DinoRun2.png'))]
jumping = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
crouching = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

small_cactus = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
large_cactus = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

cloud = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

background = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

class Dino:
    x=80
    y=310
    y_crouch = 340
    jump_vel = 8.5
    def _init_(self):

        self.crouch_img = Crouching
        self.run_img = Running
        self.jump_img = Jumping

        self.dino_crouch = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.jump_vel
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y

    def update(self,user_input):
        if self.dino_crouch:
            self.crouch()#this function is called below and defined here
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index>=10:
            self.step_index=0
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_crouch = False
            self.dino_run= False
            self.dino_jump = True
            #when up key is pressed dino_jump is set True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_crouch = True
            self.dino_run = False
            self.dino_jump = False
            #when down key is pressed dino_crouch is set True
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_crouch = False
            self.dino_run = True
            self.dino_jump = False
            #when both are not  pressed dino_run is set True
    def crouch(self):
        self.image = self.crouch_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y
        self.step_index += 1
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y
        self.step_index += 1
    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.jump_vel:
            self.dino_jump = False
            self.jump_vel = self.jump_vel
    def draw(self, SCREEN):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y)) 

class Cloud:
    def __init__(self):
        self.x = 1200 + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = cloud
        self.width = self.image.get_width()
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = 1200 + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        screen.blit(self.image, (self.x, self.y))



def game(): 
    clock=pygame.time.Clock()
    run=True
    player=Dino()
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        screen.fill(173, 216, 230)
        user_input=pygame.key.get_pressed()

        user.draw(screen)
        player.update(user_input)

        clock.tick(30)
        pygame.display.update()

  
game()