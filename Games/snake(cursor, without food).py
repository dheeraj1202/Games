import pygame #used for games in python
import sys #Used to close the program correctly
import math #maths calculations

# Initialize Pygame
pygame.init()

# to set screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Follows Mouse Cursor") #title of window

# Colors for snake and background
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Snake settings
SEGMENT_RADIUS = 10         # Fixed size
NUM_SEGMENTS = 15    # snake length(with circles count)
SEGMENT_SPACING = 20     # distance b/w each circle
SMOOTH_SPEED = 0.2  # snake speed and smoothing

# Clock
clock = pygame.time.Clock()

# starts at center of screen 
snake_segments = [(WIDTH // 2, HEIGHT // 2)] * NUM_SEGMENTS
#cursor movement
def update_snake():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # move head toward the mouse
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

    # Update all segments to follow the previous one with fixed spacing
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

def draw_snake():
    for x, y in snake_segments:
        pygame.draw.circle(screen, GREEN, (int(x), int(y)), SEGMENT_RADIUS)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    snake_segments = update_snake()

    screen.fill(BLACK)
    draw_snake()
    pygame.display.flip()
    clock.tick(60)
