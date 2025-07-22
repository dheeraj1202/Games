import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Follows Mouse with Food")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
SEGMENT_RADIUS = 10
NUM_SEGMENTS = 25
SEGMENT_SPACING = 14
SMOOTH_SPEED = 0.2

# Food settings
FOOD_RADIUS = 8

# Clock
clock = pygame.time.Clock()

# Initial snake segments
snake_segments = [(WIDTH // 2, HEIGHT // 2)] * NUM_SEGMENTS

# Create random food
def spawn_food():
    x = random.randint(FOOD_RADIUS, WIDTH - FOOD_RADIUS)
    y = random.randint(FOOD_RADIUS, HEIGHT - FOOD_RADIUS)
    return (x, y)

food_pos = spawn_food()

def update_snake():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    head_x, head_y = snake_segments[0]
    dx = mouse_x - head_x
    dy = mouse_y - head_y
    dist = math.hypot(dx, dy)

    if dist != 0:
        dx /= dist
        dy /= dist

    new_head_x = head_x + dx * SMOOTH_SPEED * dist
    new_head_y = head_y + dy * SMOOTH_SPEED * dist
    new_head = (new_head_x, new_head_y)

    new_segments = [new_head]
    for i in range(1, NUM_SEGMENTS):
        prev_x, prev_y = new_segments[i - 1]
        curr_x, curr_y = snake_segments[i]
        dx = curr_x - prev_x
        dy = curr_y - prev_y
        dist = math.hypot(dx, dy)

        if dist == 0:
            new_segments.append((curr_x, curr_y))
        else:
            dx /= dist
            dy /= dist
            new_x = prev_x + dx * SEGMENT_SPACING
            new_y = prev_y + dy * SEGMENT_SPACING
            new_segments.append((new_x, new_y))

    return new_segments

def check_food_collision(head_pos, food_pos):
    hx, hy = head_pos
    fx, fy = food_pos
    dist = math.hypot(hx - fx, hy - fy)
    return dist < SEGMENT_RADIUS + FOOD_RADIUS

def draw_snake():
    for x, y in snake_segments:
        pygame.draw.circle(screen, GREEN, (int(x), int(y)), SEGMENT_RADIUS)

def draw_food():
    pygame.draw.circle(screen, RED, (int(food_pos[0]), int(food_pos[1])), FOOD_RADIUS)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update snake
    snake_segments = update_snake()

    # Check for food collision
    if check_food_collision(snake_segments[0], food_pos):
        food_pos = spawn_food()

    # Draw everything
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    pygame.display.flip()
    clock.tick(60)
