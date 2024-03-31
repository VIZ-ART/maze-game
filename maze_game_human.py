import pygame
import random

pygame.init()

# Constants
WIDTH = 640
HEIGHT = 480
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 200)

class MazeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Maze Game')
        self.clock = pygame.time.Clock()

        # Generate a random maze layout
        self.generate_random_maze()

        # Generate random positions for the player and goal within the maze boundaries
        self.player_pos = self.find_empty_space()
        self.goal_pos = self.find_empty_space()

    def generate_random_maze(self):
        self.maze = []
        for y in range(HEIGHT // BLOCK_SIZE):
            row = []
            for x in range(WIDTH // BLOCK_SIZE):
                # Randomly choose whether to place a wall or an empty space
                if random.random() < 0.3:  # Adjust the probability as desired
                    row.append("#")  # Wall
                else:
                    row.append(" ")  # Empty space
            self.maze.append(row)

        # Ensure that the outer edges are walls
        for y in range(HEIGHT // BLOCK_SIZE):
            self.maze[y][0] = "#"
            self.maze[y][-1] = "#"
        for x in range(WIDTH // BLOCK_SIZE):
            self.maze[0][x] = "#"
            self.maze[-1][x] = "#"

    def find_empty_space(self):
        while True:
            x = random.randint(1, (WIDTH // BLOCK_SIZE) - 2)
            y = random.randint(1, (HEIGHT // BLOCK_SIZE) - 2)
            if self.maze[y][x] == " ":
                return (x, y)

    def draw_maze(self):
        self.screen.fill(WHITE)
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == "#":
                    pygame.draw.rect(self.screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_player(self):
        pygame.draw.rect(self.screen, BLUE, (self.player_pos[0] * BLOCK_SIZE, self.player_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_goal(self):
        pygame.draw.rect(self.screen, GREEN, (self.goal_pos[0] * BLOCK_SIZE, self.goal_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def move_player(self, dx, dy):
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        if 0 <= new_x < WIDTH // BLOCK_SIZE and 0 <= new_y < HEIGHT // BLOCK_SIZE:
            if self.maze[new_y][new_x] != "#":
                self.player_pos = (new_x, new_y)

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move_player(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.move_player(0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.move_player(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move_player(1, 0)
            
            if self.player_pos == self.goal_pos:
                print("Congratulations! You reached the goal!")
                # Change background to green
                for y in range(len(self.maze)):
                    for x in range(len(self.maze[y])):
                        if self.maze[y][x] == " ":
                            pygame.draw.rect(self.screen, GREEN, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.display.flip()
                pygame.time.delay(2000)  # Wait for 2 seconds
                running = False

            self.draw_maze()
            self.draw_goal()
            self.draw_player()
            pygame.display.flip()
            self.clock.tick(10)

if __name__ == "__main__":
    game = MazeGame()
    game.play()
    pygame.quit()
