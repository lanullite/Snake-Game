import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FONT_COLOR = (255, 255, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)

        self.reset()

    def reset(self):
        self.snake = [[10, 10]]
        self.direction = RIGHT
        self.score = 0
        self.spawn_food()

    def spawn_food(self):
        while True:
            self.food = [
                random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
                random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1)
            ]
            if self.food not in self.snake:
                break

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(
                self.screen,
                SNAKE_COLOR,
                pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    def draw_food(self):
        pygame.draw.rect(
            self.screen,
            FOOD_COLOR,
            pygame.Rect(self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

    def move_snake(self):
        new_head = [self.snake[0][0] + self.direction[0],
                    self.snake[0][1] + self.direction[1]]

        # Check collisions
        if (new_head in self.snake or
            new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= SCREEN_WIDTH // CELL_SIZE or
            new_head[1] >= SCREEN_HEIGHT // CELL_SIZE):
            self.game_over()
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 10
            self.spawn_food()
        else:
            self.snake.pop()

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, FONT_COLOR)
        self.screen.blit(score_text, (10, 10))

    def game_over(self):
        game_over_text = self.font.render("Game Over! Press R to Restart or Q to Quit.", True, FONT_COLOR)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 4 - 40, SCREEN_HEIGHT // 2))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        self.reset()
                        return

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

            self.screen.fill(BACKGROUND_COLOR)
            self.move_snake()
            self.draw_snake()
            self.draw_food()
            self.display_score()
            pygame.display.flip()
            self.clock.tick(10)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
