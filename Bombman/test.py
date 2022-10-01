import pygame
import sys

class Player(pygame.sprite.Sprite):
    ''' 生成玩家 '''

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
        self.movex = 0
        self.movey = 0

    def load(self, filename_prefix, begin_num, end_num,
             filename_suffix):

        self.images = [
            pygame.image.load(filename_prefix + str(v) + filename_suffix).convert()
            for v in range(begin_num, end_num + 1)
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.last_frame = end_num - 1
    def control(self, x, y):
        self.movex += x
        self.movey += y
    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey
            #向左移動
        if self.movex < 0:
            self.frame += 1
            if self.frame > 2*ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

            # 向右移动
        if self.movex > 0:
            self.frame += 1
            if self.frame > 2*ani:
                self.frame = 0
            self.image = self.images[(self.frame // ani) + 3]
            # 向上移動
        if self.movey < 0:
            self.frame += 1
            if self.frame > 2.5*ani:
                self.frame = 0
            self.image = self.images[self.frame // ani + 6]

            # 向下移动
        if self.movey > 0:
            self.frame += 1
            if self.frame > 1.5 * ani:
                self.frame = 0
            self.image = self.images[(self.frame // ani) + 9]


pygame.init()
window = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("walk")
clock = pygame.time.Clock()
ani = 3
#移動人
man = Player(window)
man.load('./control/', 1, 12, '.png')
man.rect.x = 400
man.rect.y = 300
group = pygame.sprite.Group()
group.add(man)
steps = 5
running = True
while running:

    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                man.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                man.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                man.control(0, -steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                man.control(0, steps)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                man.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                man.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                man.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                man.control(0, -steps)

    window.fill((0, 0, 0))
    group.update()
    group.draw(window)
    pygame.display.flip()
    clock.tick(30)