import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Follows Mouse")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Snake segment settings
SEGMENT_RADIUS = 10
SEGMENT_DISTANCE = 15
NUM_SEGMENTS = 30

# Clock
clock = pygame.time.Clock()

# Create initial snake segments
snake_segments = [(WIDTH // 2, HEIGHT // 2)] * NUM_SEGMENTS

def follow_mouse():
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Move the head towards the mouse
    head_x, head_y = snake_segments[0]
    dx = mouse_x - head_x
    dy = mouse_y - head_y
    distance = math.hypot(dx, dy)

    if distance > 0:
        dx /= distance
        dy /= distance

    new_head = (head_x + dx * SEGMENT_DISTANCE, head_y + dy * SEGMENT_DISTANCE)

    # Move each segment to the position of the one before it
    for i in range(NUM_SEGMENTS - 1, 0, -1):
        snake_segments[i] = snake_segments[i - 1]
    snake_segments[0] = new_head

def draw_snake():
    for segment in snake_segments:
        pygame.draw.circle(screen, GREEN, (int(segment[0]), int(segment[1])), SEGMENT_RADIUS)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    follow_mouse()

    screen.fill(BLACK)
    draw_snake()
    pygame.display.flip()
    clock.tick(60)
