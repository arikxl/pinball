import pygame
import keyboard
import random

# Initialize pygame
pygame.init()

# Constants for screen dimensions
HEIGHT = 700
WIDTH = 500

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pinball")

# Clock and FPS
clock = pygame.time.Clock()
FPS = 25

# Fonts
font = pygame.font.SysFont("none", 60)

# Load images and get their rectangles
BG = pygame.image.load("bg.jpg").convert()

pt10 = pygame.image.load("10.png")
pt10_rect = pt10.get_rect()
pt10_rect.centerx = WIDTH//2
pt10_rect.centery = 50

pt20 = pygame.image.load("20.png")
pt20_rect = pt20.get_rect()
pt20_rect.centerx = 80
pt20_rect.centery = 150

pt30 = pygame.image.load("30.png")
pt30_rect = pt30.get_rect()
pt30_rect.centerx = 400
pt30_rect.centery = 170

ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect(center=(WIDTH // 2, HEIGHT // 2))
dx = 10
dy = 10 * random.choice([-1, 1])

paddle = pygame.image.load("paddleL.png")
paddle_rect = paddle.get_rect()
paddle_rect.centerx = 80
paddle_rect.centery = HEIGHT - 100



paddle2 = pygame.image.load("paddleR.png")
paddle2_rect = paddle2.get_rect()
paddle2_rect.centerx = WIDTH - 80
paddle2_rect.centery = HEIGHT - 100




# Score and lives
score = 0
live = 3

# Game state
running = True

# Paddle rotation angle
angle1 = 20
angle2 = 20

# Game loop
while running:
    win.blit(BG, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            WIDTH = event.w
            HEIGHT = event.h
            win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    #ball and paddles
    win.blit(ball, ball_rect)
    rot1 = pygame.transform.rotate(paddle, angle1)
    rot1_rect = rot1.get_rect(center=paddle_rect.center)
    win.blit(rot1, rot1_rect)

    rot2 = pygame.transform.rotate(paddle2, angle2)
    rot2_rect = rot2.get_rect(center=paddle2_rect.center)
    win.blit(rot2, rot2_rect)

    # ball
    ball_rect.x += dx
    ball_rect.y += dy
    if ball_rect.right >= WIDTH:
        ball_rect.right = WIDTH
        dx *= random.choice([-1, 1])

    elif ball_rect.left <= 0:
        ball_rect.left = 0
        dx *= random.choice([-1, 1])

    elif ball_rect.top <= 0:
        dy *= -1
    elif ball_rect.bottom >= HEIGHT:
        live -= 1
        ball_rect.y = 20
    # paddle movement
    if keyboard.is_pressed("right"):
        angle2 -= 10
        angle2 = max(angle2, -50)
    else:
        angle2 = 25

    if keyboard.is_pressed("left"):
        angle1 += 10
        angle1 = min(angle1, 50)
    else:
        angle1 = -25

    # collision detection
    if ball_rect.colliderect(rot1_rect) or ball_rect.colliderect(rot2_rect):
        dy *= -1

    win.blit(pt10, pt10_rect)
    win.blit(pt20, pt20_rect)
    win.blit(pt30, pt30_rect)

    if ball_rect.colliderect(pt10_rect):
        score += 10
        dx *= random.choice([-1, 1])
        dy *= -1
    elif ball_rect.colliderect(pt20_rect):
        score += 20
        dx *= random.choice([-1, 1])
        dy *= -1
    elif ball_rect.colliderect(pt30_rect):
        score += 30
        dx *= random.choice([-1, 1])
        dy *= -1


    # blit scores and lives
    text = font.render(f"Score: {score}", True, "white")
    lives = font.render(f"Lives: {live}", True, "white")
    win.blit(text, (0, 30))
    win.blit(lives, (0, 80))

    # check for game over
    if live < 0:
        win.fill("blue")
        lose = font.render("Lose", True, "white")
        win.blit(lose, (WIDTH//2, HEIGHT//2))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
