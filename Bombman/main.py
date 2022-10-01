import sys
import pygame

class Walk(pygame.sprite.Sprite):
    def __init__(self, scene):
        pygame.sprite.Sprite.__init__(self)
        self.main_scene = scene
        self.image = None
        self.rect = None
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.images = []
        self.last_time = pygame.time.get_ticks()

    def load(self, filename_prefix, begin_num, end_num,
                    filename_suffix):

        self.images = [
            pygame.image.load(filename_prefix + str(v) + filename_suffix).convert()
            for v in range(begin_num, end_num + 1)
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.last_frame = end_num - 1

    def setpos(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
            self.image = self.images[self.frame]
            if self.rect.x < -50:
                self.rect.x = 820
            self.rect.x-=10
class Spark(pygame.sprite.Sprite):
    def __init__(self, scene):
        pygame.sprite.Sprite.__init__(self)
        self.main_scene = scene
        self.image = None
        self.rect = None
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.images = []
        self.last_time = pygame.time.get_ticks()
        self.rate = 150

    def load(self, filename_prefix, begin_num, end_num,
                    filename_suffix):

        self.images = [
            pygame.image.load(filename_prefix + str(v) + filename_suffix)
            for v in range(begin_num, end_num + 1)
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.last_frame = end_num - 1

    def setpos(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
            self.image = self.images[self.frame]


pygame.init()
window = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("walk")
font = pygame.font.Font(None, 18)
clock = pygame.time.Clock()

bg = "bg.png"
background = pygame.image.load(bg).convert_alpha()

#按鈕start
button = Spark(window)
button.load('./bt/',1,2,'.png')
button.setpos(280,430)
bgroup = pygame.sprite.Group()
bgroup.add(button)
#水球
ball = Spark(window)
ball.load('./ball/',1,7,'.png')
ball.setpos(490,85)
ballgroup = pygame.sprite.Group()
ballgroup.add(ball)
ball2 = Spark(window)
ball2.load('./ball/bomb',1,8,'.png')
ball2.setpos(560,230)
ballgroup2 = pygame.sprite.Group()
ballgroup2.add(ball2)
#移動人
man = Walk(window)
man.load('./pic/', 1, 3, '.png')
man.setpos(800,545)
group = pygame.sprite.Group()
group.add(man)
running = True
while running:
    clock.tick(30)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        exit()
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    bgroup.update(ticks,400)
    ballgroup.update(ticks,150)
    ballgroup2.update(ticks, 150)
    group.update(ticks, 150)
    bgroup.draw(window)
    ballgroup.draw(window)
    ballgroup2.draw(window)
    group.draw(window)
    pygame.display.update()