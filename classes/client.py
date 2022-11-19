import pygame

from classes.entity.Rocket import Rocket
from classes.managers.DisplayManager import DisplayManager
from classes.managers.EventManager import EventManager

from utils.logger import Logger
from utils.utils import Clock


class Client:
    def __init__(self, resolution, title, fps):
        self._resolution = resolution
        self._title = title

        self._screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)

        self._run = True

        self._displayManager = DisplayManager(debug=True)
        self._eventManager = EventManager()
        self._logger = Logger()

        self._entities = [Rocket()]

        self._fps = fps
        self.clock = Clock(self._fps)

    def run(self):
        while self._run:
            self._screen.blit(self.tick(), (0, 0))

            pygame.display.update()

    def tick(self):
        events = self._eventManager.update(pygame.event.get(), self)

        for entity in self._entities:
            entity.update(events)
        
        for entity in self._entities:
            if entity.name == 'Rocket':
                self._logger.send_data_tcp(entity)

        return self._displayManager.update(self._screen.get_size(), self._entities)