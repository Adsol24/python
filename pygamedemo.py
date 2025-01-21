import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Action Game")

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60

player = pygame.Rect(100, 500, 50, 50)
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
