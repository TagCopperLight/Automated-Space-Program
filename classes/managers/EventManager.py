import pygame


class Event:
    def __init__(self):
        self.closed = False

        self.keys_down = []
        
        self.keys_up = []


class EventManager:
    def __init__(self):
        pass

    def update(self, events, client):
        returned_event = Event()

        for event in events:
            if event.type == pygame.QUIT:
                    client._run = False
            if event.type == pygame.KEYDOWN:
                returned_event.keys_down.append(event.key)
            if event.type == pygame.KEYUP:
                returned_event.keys_up.append(event.key)
        
        return returned_event