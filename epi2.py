import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Define the variables for the simulation
POPULATION_SIZE = 200
MOVEMENT_RATE = 5
PROBABILITY_OF_TRANSMISSION = 0.2
LENGTH_OF_CONTAGIOUSNESS = 10
LENGTH_OF_ILLNESS = 14
PROBABILITY_OF_DEATH = 0.05

# Define the class for the person
class Person(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contagious_timer = 0
        self.illness_timer = 0
        self.is_contagious = False
        self.is_ill = False
        self.is_dead = False

    def update(self):
        # Move the person
        self.rect.x += random.randint(-MOVEMENT_RATE, MOVEMENT_RATE)
        self.rect.y += random.randint(-MOVEMENT_RATE, MOVEMENT_RATE)

        # Check if the person is contagious
        if self.is_contagious:
            self.contagious_timer += 1
            if self.contagious_timer >= LENGTH_OF_CONTAGIOUSNESS:
                self.is_contagious = False

        # Check if the person is ill
        if self.is_ill:
            self.illness_timer += 1
            if self.illness_timer >= LENGTH_OF_ILLNESS:
                self.is_ill = False
                self.is_dead = random.random() < PROBABILITY_OF_DEATH

    def set_contagious(self):
        self.is_contagious = True

    def set_ill(self):
        self.is_ill = True

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Disease Spread Simulation')

# Create a group of all sprites
all_sprites_group = pygame.sprite.Group()

# Create a group of contagious sprites
contagious_sprites_group = pygame.sprite.Group()

# Create the population of people
for i in range(POPULATION_SIZE):
    person = Person(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    all_sprites_group.add(person)

# Set a random person to be contagious
contagious_person = random.choice(all_sprites_group.sprites())
contagious_person.set_contagious()
contagious_sprites_group.add(contagious_person)

# Run the simulation
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites_group.update()

    # Check for collisions between contagious and non-contagious people
    for person in pygame.sprite.groupcollide(all_sprites_group, contagious_sprites_group, False, False).keys():
        if not person.is_contagious and not person.is_ill and not person.is_dead:
            if random.random() < PROBABILITY_OF_TRANSMISSION:
                person.set_contagious()
                contagious_sprites_group.add(person)

    # Draw the background
    screen.fill(BLACK)

    # Draw all the sprites
    all_sprites_group.draw(screen)

    # Draw a red circle around contagious people
    for person in contagious_sprites_group:
        pygame.draw.circle(screen, RED, [person.rect.x + 5, person.rect.y + 5], 15, 2)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()