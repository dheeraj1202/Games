import tkinter as tk
import random

# Game window size
WIDTH = 1000
HEIGHT = 500
GRID_SIZE = 20

# Colors of game
BG_COLOR = "black"
SNAKE_COLOR = "lime"
FOOD_COLOR = "red"
TEXT_COLOR = "white"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Snake Game")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()
        
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake position
        self.food = self.spawn_food()
        self.direction = "Right"
        self.score = 0
        
        self.running = True
        self.update()
    
    def spawn_food(self):
        while True:
            x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
            y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
            if (x, y) not in self.snake:
                return (x, y)
    
    def move_snake(self):
        if not self.running:
            return
        
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food
        
        # Smart movement to avoid collisions
        if head_x < food_x and (head_x + GRID_SIZE, head_y) not in self.snake:
            self.direction = "Right"
        elif head_x > food_x and (head_x - GRID_SIZE, head_y) not in self.snake:
            self.direction = "Left"
        elif head_y < food_y and (head_x, head_y + GRID_SIZE) not in self.snake:
            self.direction = "Down"
        elif head_y > food_y and (head_x, head_y - GRID_SIZE) not in self.snake:
            self.direction = "Up"
        
        if self.direction == "Up":
            head_y -= GRID_SIZE
        elif self.direction == "Down":
            head_y += GRID_SIZE
        elif self.direction == "Left":
            head_x -= GRID_SIZE
        elif self.direction == "Right":
            head_x += GRID_SIZE
        
        new_head = (head_x, head_y)
        
        # Check for collisions
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in self.snake):
            self.running = False
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill=TEXT_COLOR, font=("Arial", 24, "bold"))
            return
        
        self.snake.insert(0, new_head)
        
        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 1
        else:
            self.snake.pop()
    
    def update(self):
        if self.running:
            self.move_snake()
            self.draw()
            speed = max(50, 1 - (self.score * 5))  # Increase speed as score goes up
            self.root.after(speed, self.update)
    
    def draw(self):
        self.canvas.delete("all")
        
        # Draw food
        x, y = self.food
        self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=FOOD_COLOR)
        
        # Draw snake
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR)
        
        # Display score
        self.canvas.create_text(50, 20, text=f"Score: {self.score}", fill=TEXT_COLOR, font=("Arial", 16, "bold"))
        
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()