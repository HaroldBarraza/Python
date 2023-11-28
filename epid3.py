import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
width = 800
height = 600

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set simulation variables
population_size = 100
movement_rate = 2
transmission_probability = 10
contagiousness_length = 100
illness_length = 200
death_probability = 0.08

# Define a class for simulating individuals
class Individual(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = "healthy"
        self.contagiousness_counter = 0
        self.illness_counter = 0
        self.is_contagious = False
        self.is_ill = False
        self.is_dead = False

    def update(self):
        # Move the person
        self.rect.x += random.randint(-movement_rate, movement_rate)
        self.rect.y += random.randint(-movement_rate, movement_rate)

        # Check if the person is contagious
        if self.is_contagious:
            self.contagiousness_counter += 1
            if self.contagiousness_counter >= contagiousness_length:
                self.is_contagious = False

        # Check if the person is ill
        if self.is_ill:
            self.illness_counter += 1
            if self.illness_counter >= illness_length:
                self.is_ill = False
                self.is_dead = random.random() < death_probability

        # Update the individual's state based on infection status
        if self.state == "infected":
            self.contagiousness_counter += 1
            if self.contagiousness_counter >= contagiousness_length:
                self.state = "recovered"
        elif self.state == "recovered":
            self.illness_counter += 1
            if self.illness_counter >= illness_length:
                if random.random() < death_probability:
                    self.state = "dead"
                else:
                    self.state = "healthy"
                    self.contagiousness_counter = 0
                    self.illness_counter = 0

    def infect(self):
        if self.state == "healthy":
            if random.random() < transmission_probability:
                self.state = "infected"
                self.contagiousness_counter = 0

# Set up the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Disease Spread Simulation")

# Create a group of all sprites
all_sprites_group = pygame.sprite.Group()

# Create a group of contagious sprites
contagious_sprites_group = pygame.sprite.Group()

# Create the population of people
for i in range(population_size):
    person = Individual(random.randint(0, width), random.randint(0, height))
    all_sprites_group.add(person)

    # Set a random person to be contagious
    if i == 0:
        person.is_contagious = True
        contagious_sprites_group.add(person)

# Run the simulation
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and move individuals
    for individual in all_sprites_group:
        individual.update()
        individual.rect.x += random.randint(-movement_rate, movement_rate)
        individual.rect.y += random.randint(-movement_rate, movement_rate)

        # Check for collisions between individuals
        collisions = pygame.sprite.spritecollide(individual, all_sprites_group, False)
        for collision in collisions:
            if collision != individual:
                if collision.is_contagious and individual.state == "healthy":
                    individual.is_contagious = True

    # Draw the background
    window.fill(blue)

    # Draw all the sprites
    all_sprites_group.draw(window)

    # Draw a red circle around contagious people
    for person in contagious_sprites_group:
        pygame.draw.circle(window, red, [person.rect.x + 5, person.rect.y + 5], 15, 2)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
