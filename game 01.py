import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 4
ball_speed_y = -4

paddle_width = 100
paddle_height = 15
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 40
paddle_speed = 10

brick_rows = 6
brick_cols = 8
brick_width = WIDTH // brick_cols
brick_height = 30

bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_rect = pygame.Rect(col * brick_width, row * brick_height, brick_width - 2, brick_height - 2)
        bricks.append(brick_rect)

font = pygame.font.SysFont("Arial", 30)

score = 0

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ball_speed_x *= -1
    if ball_y <= ball_radius:
        ball_speed_y *= -1
    if ball_y > HEIGHT:
        running = False

    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.collidepoint(ball_x, ball_y + ball_radius):
        ball_speed_y *= -1

    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y - ball_radius):
            bricks.remove(brick)
            ball_speed_y *= -1
            score += 10
            break

    screen.fill(BLACK)

    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    pygame.draw.rect(screen, GREEN, paddle_rect)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, HEIGHT - 30))

    pygame.display.flip()

pygame.quit()
sys.exit()


