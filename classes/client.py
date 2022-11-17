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
        self.rocket = Rocket()

        self._fps = fps
        self.clock = Clock(self._fps)

    def run(self):
        while self._run:
            self._screen.blit(self.tick(), (0, 0))

            pygame.display.update()

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.rocket.set_thrust(self.rocket.thrust - 1)
                if event.key == pygame.K_z:
                    self.rocket.set_thrust(self.rocket.thrust + 1)
                # if event.key == pygame.K_SPACE:
                #     enable_pid = not enable_pid

        self._screen.fill(Colors.SKY.value)

        # if enable_pid:
        #     self.rocket.rotation.rotate_ip(0.5)

        self.rocket.update()

        if self.rocket.position.y <= 75:
            self.rocket.position.y = 75
            self.rocket.velocity = pygame.Vector2()
        
        self._logger.send_data_tcp(self.rocket)

        return self._display.update(self._screen.get_size(), self.rocket)