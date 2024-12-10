import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atari Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

player1 = pygame.Rect(10, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 20, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

player_speed = 6
ball_speed_x = random.choice([-5, 5])
ball_speed_y = random.choice([-5, 5])

player1_score = 0
player2_score = 0

font = pygame.font.Font(None, 74)
menu_font = pygame.font.Font(None, 50)

def draw_elements():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH // 4, 20))
    screen.blit(player2_text, (WIDTH * 3 // 4, 20))

def move_ai():
    if ball.centery > player2.centery:
        player2.y += player_speed
    elif ball.centery < player2.centery:
        player2.y -= player_speed
    player2.y = max(0, min(player2.y, HEIGHT - PADDLE_HEIGHT))

def menu_screen():
    while True:
        screen.fill(BLACK)
        title_text = menu_font.render("Atari Pong", True, WHITE)
        play_ai_text = menu_font.render("1. Play with AI", True, WHITE)
        play_player_text = menu_font.render("2. Play against Player", True, WHITE)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        screen.blit(play_ai_text, (WIDTH // 2 - play_ai_text.get_width() // 2, HEIGHT // 2))
        screen.blit(play_player_text, (WIDTH // 2 - play_player_text.get_width() // 2, HEIGHT // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return True
                if event.key == pygame.K_2:
                    return False

play_with_ai = menu_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= player_speed
    if keys[pygame.K_s]:
        player1.y += player_speed
    if not play_with_ai:
        if keys[pygame.K_UP]:
            player2.y -= player_speed
        if keys[pygame.K_DOWN]:
            player2.y += player_speed

    player1.y = max(0, min(player1.y, HEIGHT - PADDLE_HEIGHT))
    if not play_with_ai:
        player2.y = max(0, min(player2.y, HEIGHT - PADDLE_HEIGHT))

    if play_with_ai:
        move_ai()

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    if ball.left <= 0:
        player2_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice([-1, 1.05])
        ball_speed_y *= random.choice([-1, 1.05])

    if ball.right >= WIDTH:
        player1_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice([-1, 1.05])
        ball_speed_y *= random.choice([-1, 1.05])

    if player1_score == 11 or player2_score == 11:
        running = False

    draw_elements()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
