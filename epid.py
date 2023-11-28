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
population_size = 200
movement_rate = 2
transmission_probability = 0.5
contagiousness_length = 100
illness_length = 200
death_probability = 0.05
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
    
    def update(self):
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
    
    def move(self):
        self.rect.x += random.randint(-movement_rate, movement_rate)
        self.rect.y += random.randint(-movement_rate, movement_rate)
        
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > width:
            self.rect.x = width
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > height:
            self.rect.y = height
    
    def infect(self):
        if self.state == "healthy":
            if random.random() < transmission_probability:
                self.state = "infected"
                self.contagiousness_counter = 0
# Create a population of individuals
population = pygame.sprite.Group()
for _ in range(population_size):
    x = random.randint(0, width)
    y = random.randint(0, height)
    individual = Individual(x, y)
    population.add(individual)
# Set up the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Epid Simulation")
# Run the simulation
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(blue)
    
    # Update and move individuals
    for individual in population:
        individual.update()
        individual.move()
        
        # Check for collisions between individuals
        collisions = pygame.sprite.spritecollide(individual, population, False)
        for collision in collisions:
            if collision != individual:
                individual.infect()
    
    # Draw individuals on the window
    for individual in population:
        if individual.state == "infected":
            color = red
        elif individual.state == "recovered":
            color = green
        elif individual.state == "dead":
            color = black
        else:
            color = white
        pygame.draw.rect(window, color, individual.rect)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()