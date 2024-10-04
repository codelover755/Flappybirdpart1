import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.update()

bg1 = pygame.image.load(r"Game dev 2\flappy bird sprites\background.png")
bg = pygame.transform.scale(bg1,(600,600))
gr = pygame.image.load(r"Game dev 2\flappy bird sprites\Ground.png")

v = 0
fps = 60
clock = pygame.time.Clock()

screen.blit(bg,(0,0))
pygame.display.update()

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(gr,(v,570))
    v = v - 2
    if v < -200:
        v = 0
    

    pygame.display.update()