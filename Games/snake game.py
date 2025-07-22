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

class SnakeGame:
    def __init__(self, root):
        self.root = root  # new window will be open for game
        self.root.title("Snake Game(By Dheeraj)")  #page title
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR) # this is for gamepage 
        self.canvas.pack()
        
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake position in game
        self.food = self.spawn_food() # spawn means random food
        self.direction = "Right" # when game starts moves to right
        self.score = 0 #stating score
        
        self.running = True # runs automatically
        self.update()
        
        self.root.bind("<KeyPress>", self.change_direction) #changes the direction by pressing arrows
        
    def spawn_food(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE #by this food will located
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE #by this food will located
        return (x, y)
    
    def change_direction(self, event): # key directions
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if self.direction != opposite_directions.get(event.keysym, ""):
                self.direction = event.keysym
    
    def move_snake(self):
        if not self.running:
            return
        
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= GRID_SIZE
        elif self.direction == "Down":
            y += GRID_SIZE
        elif self.direction == "Left":
            x -= GRID_SIZE
        elif self.direction == "Right":
            x += GRID_SIZE
        
        new_head = (x, y)
        
        # Check for collisions
        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in self.snake):
            self.running = False
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="white", font=("Arial", 24, "bold"))
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
            self.root.after(150, self.update)  # Control the speed of the snake
    
    def draw(self):
        self.canvas.delete("all")
        
        # To make food
        x, y = self.food
        self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=FOOD_COLOR)
        
        # To make snake
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR)
# starts game here
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
