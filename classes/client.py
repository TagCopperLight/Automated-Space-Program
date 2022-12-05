import pygame # pyright: reportImportCycles=false

from classes.entity.Rocket import Rocket
from classes.managers.DisplayManager import DisplayManager
from classes.managers.EventManager import EventManager

from classes.entity.parts.FuelTank import FuelTank
from classes.entity.parts.Engine import Engine
from classes.entity.parts.Fairing import Fairing
from classes.entity.Entity import Entity

from utils.logger import Logger
from utils.utils import Clock


class Client:
    def __init__(self, resolution : tuple[int, int], title : str, fps : int) -> None:
        self._resolution = resolution
        self._title = title

        self._screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)

        self.running = True

        self._displayManager = DisplayManager(debug=True)
        self._eventManager = EventManager()
        self._logger = Logger(activate=False)

        self._entities : list[Entity] = [Rocket([Engine(), FuelTank(), FuelTank(), FuelTank(), FuelTank(), Fairing()], self._displayManager)]

        self._fps = fps
        self.clock = Clock(self._fps)

        self.pause = False

    def run(self) -> None:
        while self.running:
            self._screen.blit(self.tick(), (0, 0))
            if not self.pause:
                pygame.display.update()

    def tick(self) -> pygame.Surface:
        events = self._eventManager.update(pygame.event.get(), self)

        for entity in self._entities:
            entity.update(events)
        
        if 112 in events.keys_down:
            self.pause = not self.pause
        
        for entity in self._entities:
            if entity.name == 'Rocket':
                self._logger.send_data_tcp(entity) #type: ignore

        return self._displayManager.update(self._screen.get_size(), self._entities)