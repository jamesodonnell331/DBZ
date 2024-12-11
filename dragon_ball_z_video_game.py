#My Dragon Ball Z Video Game (example pygame basics from Grok2)
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dragon Ball Z Fighter')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player attributes
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
    
    def update(self):
        # Basic movement (you'll need to expand this with more controls)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        # Keep player on screen
        self.rect.clamp_ip(screen.get_rect())

    def draw_health(self, health_bar):
        pygame.draw.rect(health_bar, RED, (0, 0, self.health, 20))

# Load sprites for Goku and Vegeta
goku = Player(100, 400, 'goku.png')
vegeta = Player(600, 400, 'vegeta.png')

all_sprites = pygame.sprite.Group(goku, vegeta)

# Create surfaces for health bars
goku_health_bar = pygame.Surface((100, 20))
vegeta_health_bar = pygame.Surface((100, 20))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    # Draw health bars
    goku_health_bar.fill(BLACK)
    vegeta_health_bar.fill(BLACK)
    goku.draw_health(goku_health_bar)
    vegeta.draw_health(vegeta_health_bar)
    screen.blit(goku_health_bar, (50, 10))
    screen.blit(vegeta_health_bar, (width - 150, 10))

    # Update display
    pygame.display.flip()

    # Control game speed
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()