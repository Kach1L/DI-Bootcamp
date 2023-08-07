import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Display settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math24➕➖✖️➗2️⃣4️⃣")

# Colors
DARK_BLUE = (0, 0, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Shape and symbol settings
SHAPE_SIZE = 130
SHAPE_SPACING = 50

class GameScreen:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.shapes = []
        self.symbols = ["+", "-", "*", "/"]
        self.init_shapes()

    def init_shapes(self):
        for row in range(2):
            for col in range(2):
                value = random.randint(1, 9)  # Random integer value for the square
                square_x = col * (SHAPE_SIZE + SHAPE_SPACING) + (WIDTH - 2 * (SHAPE_SIZE + SHAPE_SPACING)) / 2
                square_y = row * (SHAPE_SIZE + SHAPE_SPACING) + (HEIGHT - 2 * (SHAPE_SIZE + SHAPE_SPACING)) / 2
                self.shapes.append((value, RED, square_x, square_y))

    def draw(self):
        screen.fill(DARK_BLUE)

        for shape_value, shape_color, shape_x, shape_y in self.shapes:
            pygame.draw.rect(screen, shape_color, (shape_x, shape_y, SHAPE_SIZE, SHAPE_SIZE))
            font = pygame.font.Font(None, 36)
            text_surface = font.render(str(shape_value), True, WHITE)
            text_rect = text_surface.get_rect(center=(shape_x + SHAPE_SIZE / 2, shape_y + SHAPE_SIZE / 2))
            screen.blit(text_surface, text_rect)

        for i, symbol in enumerate(self.symbols):
            circle_x = (i + 1) * (WIDTH // (len(self.symbols) + 1))
            circle_y = HEIGHT - SHAPE_SIZE // 2 - 10
            pygame.draw.circle(screen, WHITE, (circle_x, circle_y), SHAPE_SIZE // 2)
            font = pygame.font.Font(None, 50)
            text_surface = font.render(symbol, True, DARK_BLUE)
            text_rect = text_surface.get_rect(center=(circle_x, circle_y))
            screen.blit(text_surface, text_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i, (_, _, shape_x, shape_y) in enumerate(self.shapes):
                        if shape_x <= mouse_x <= shape_x + SHAPE_SIZE and shape_y <= mouse_y <= shape_y + SHAPE_SIZE:
                            self.shapes[i] = (self.shapes[i][0], ORANGE, shape_x, shape_y)
                            pygame.display.flip()
                            time.sleep(1)
                            print(f"Clicked on {self.shapes[i][0]}")
                            self.shapes[i] = (self.shapes[i][0], RED, shape_x, shape_y)

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = GameScreen()
    game.run()