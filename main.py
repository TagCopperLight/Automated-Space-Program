import pygame

from classes.pid import PID
from classes.rocket import Rocket
from classes.colors import Colors
from classes.display import Display
from classes.graph import Graph

from utils.utils import Clock, get_time

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
display = Display(debug=True)
graph = Graph()

FPS = 60

rocket = Rocket(screen.get_width() // 2, 75)
pid = PID(1, 0.001, 200)

desired_altitude = 200

enable_pid = False
running = True
printed = False

clock = Clock(FPS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                rocket.set_thrust(rocket.thrust - .1)
            if event.key == pygame.K_z:
                rocket.set_thrust(rocket.thrust + .1)
            if event.key == pygame.K_SPACE:
                enable_pid = not enable_pid

    screen.fill(Colors.SKY.value)

    if enable_pid:
        rocket.set_thrust(-pid.update(desired_altitude - rocket.position.y) / 100)

    rocket.update()
    
    if rocket.position.y <= 75:
        rocket.position.y = 75
        rocket.velocity = pygame.Vector2()

    screen.blit(display.update(screen.get_size(), rocket, desired_altitude), (0, 0))
    graph.update(rocket)

    pygame.display.update()

    clock.sleep()

graph.show()