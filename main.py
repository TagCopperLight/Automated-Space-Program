import pygame
import time
import matplotlib.pyplot as plt

from classes.pid import PID
from classes.rocket import Rocket
from classes.colors import Colors
from classes.display import Display
from classes.graph import Graph

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
display = Display(debug=True)
graph = Graph()

rocket = Rocket(screen.get_width() // 2, 5000)
pid = PID(1, 0.001, 200)

desired_altitude = 200

enable_pid = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                desired_altitude += 25
            if event.key == pygame.K_DOWN:
                desired_altitude -= 25
            if event.key == pygame.K_s:
                rocket.thrust -= 0.1
            if event.key == pygame.K_z:
                rocket.thrust += 0.1
            if event.key == pygame.K_SPACE:
                enable_pid = not enable_pid

    screen.fill(Colors.SKY.value)

    if enable_pid:
        rocket.set_thrust(pid.update(desired_altitude - rocket.position.y) / 100)

    rocket.update(clock.get_time() / 16 / 60)
    if rocket.position.y <= 75:
        rocket.position.y = 75
        rocket.velocity = pygame.Vector2()
    screen.blit(display.update(screen.get_size(), rocket, desired_altitude), (0, 0))
    graph.update(rocket, desired_altitude)

    pygame.display.update()
    
    clock.tick(60)

graph.show()