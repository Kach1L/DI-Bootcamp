import pygame
import sys

# Initialize Pygame
pygame.init()

class GameScreen:
    def __init__(self):
        # Screen dimensions
        WIDTH, HEIGHT = 800, 600

        # Colors
        back_blue = (9, 0, 87)
        yellow = (233, 219, 0)
        red = (255, 0, 0)
        white = (255,255,255)
        
        # Shape and symbol settings
        SHAPE_SIZE = 140
        SHAPE_SPACING = 50

        # Create the screen
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Math24➕➖✖️➗2️⃣4️⃣")

        clock = pygame.time.Clock()

        # Function to check if a point is inside a circle
        # def point_inside_circle(x, y, circle_x, circle_y, radius):
        #     return (x - circle_x)**2 + (y - circle_y)**2 <= radius**2

        # Main loop
        def main():
            clock = pygame.time.Clock()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    screen.fill(back_blue)
                    
        # Draw squares
        for row in range(2):
            for col in range(2):
                square_x = col * (SHAPE_SIZE + SHAPE_SPACING) + (WIDTH - 2 * (SHAPE_SIZE + SHAPE_SPACING)) / 2
                square_y = row * (SHAPE_SIZE + SHAPE_SPACING) + (HEIGHT - 2 * (SHAPE_SIZE + SHAPE_SPACING)) / 2
                pygame.draw.rect(screen, red, (square_x, square_y, SHAPE_SIZE, SHAPE_SIZE))

                # Draw circles with symbols
                symbols = ["+", "-", "x", "÷"]
                for i, symbol in enumerate(symbols):
                    circle_x = (i + 1) * (WIDTH // (len(symbols) + 1))
                    circle_y = HEIGHT - SHAPE_SIZE // 2 - 10
                    pygame.draw.circle(screen, red, (circle_x, circle_y), SHAPE_SIZE // 2)
                    font = pygame.font.Font(None, 50)
                    text_surface = font.render(symbol, True, white)
                    text_rect = text_surface.get_rect   (center=(circle_x, circle_y))
                    screen.blit(text_surface, text_rect)
        
                pygame.display.flip()
                clock.tick(60)

        if __name__ == "__main__":
            main()
        pygame.quit()
        sys.exit()
Game1=GameScreen()
Game1.__init__()



