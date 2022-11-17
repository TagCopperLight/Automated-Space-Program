import pygame

from classes.entity.rocket import Rocket
from utils.colors import Colors
from classes.display import Display
from classes.logger import Logger

from utils.utils import Clock


class Client:
    def __init__(self, resolution, title, fps):
        self._resolution = resolution
        self._title = title

        self._screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)

        self._run = True

        self._display = Display(debug=True)
        self._logger = Logger()

        self._entities = [Rocket()]

        self._fps = fps
        self.clock = Clock(self._fps)

    def run(self):
        while self._run:
            self._screen.blit(self.tick())

            pygame.display.update()

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    rocket.set_thrust(rocket.thrust - 1)
                if event.key == pygame.K_z:
                    rocket.set_thrust(rocket.thrust + 1)
                if event.key == pygame.K_SPACE:
                    enable_pid = not enable_pid

        self._screen.fill(Colors.SKY.value)

        if enable_pid:
            rocket.rotation.rotate_ip(0.5)

        rocket.update()

        if rocket.position.y <= 75:
            rocket.position.y = 75
            rocket.velocity = pygame.Vector2()

        graph.update(rocket)
        graph.send_data(rocket)


        return self._display.update(self._screen.get_size(), rocket, desired_altitude, (0, 0))