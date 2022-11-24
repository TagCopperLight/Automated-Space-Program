from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import Client

import pygame

from classes.Event import Event

class EventManager:
    def update(self, events : list[pygame.event.Event], client : 'Client') -> Event:
        returned_event = Event()

        for event in events:
            if event.type == pygame.QUIT:
                    client.running = False
            if event.type == pygame.KEYDOWN:
                returned_event.keys_down.append(event.key)
            if event.type == pygame.KEYUP:
                returned_event.keys_up.append(event.key)
        
        return returned_event