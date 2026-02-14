import pygame
import sys

# Initialize pygame
pygame.init()

# 1. Window size (500, 500)
screen = pygame.display.set_mode((500, 500))

# 2. Set caption
pygame.display.set_caption("My first game screen")

# 4. Background colour (Grey: 58, 58, 58)
background_color = (58, 58, 58)

# 3. Load and resize image to (300, 300)
image = pygame.image.load("07.02.2026/image.jpg")  # Make sure image.png is in the same folder
image = pygame.transform.scale(image, (300, 300))

# Get rectangle for centering the image
image_rect = image.get_rect(center=(250, 250))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(background_color)

    # Draw image at centre
    screen.blit(image, image_rect)

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
