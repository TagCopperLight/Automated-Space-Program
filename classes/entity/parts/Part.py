from pygame import Vector2

from classes.entity.Entity import Entity


class Part(Entity):
    def __init__(self):
        super().__init__()

        self.name = "Part"

        self.sprite = None
    
    def get_sprite(self):
        return self.sprite
    
    def get_application_points(self, rotation, velocity):
        return []
    
    def get_applied_force(self, application_point, velocity, density):
        return Vector2()