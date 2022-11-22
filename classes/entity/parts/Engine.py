from pygame import Vector2

from classes.entity.parts.Part import Part


class Engine(Part):
    def __init__(self):
        super().__init__()

        self.name = "Engine"
        self.sprite = 'data/parts/engine.png'

        self.mass = 4410
        self.size = Vector2(4, 4)

        self.starting_points = [self.position + Vector2(0, self.size.y / 2), self.position + self.size / 2, self.position + Vector2(-self.size.x / 2, self.size.y / 2)]
        self.faces = [
            [self.position + Vector2(-self.size.x / 2, 0), self.position + Vector2(self.size.x / 2, 0), self.position],
            [self.position + Vector2(self.size.x / 2, 0), self.position + Vector2(self.size.x / 2, self.size.y), self.position + self.size / 2],
            [self.position + Vector2(self.size.x / 2, self.size.y), self.position + Vector2(-self.size.x / 2, self.size.y), self.position + Vector2(0, self.size.y)],
            [self.position + Vector2(-self.size.x / 2, self.size.y), self.position + Vector2(-self.size.x / 2, 0), self.position + Vector2(-self.size.x / 2, self.size.y / 2)]
            ]
        
        self.moment_of_inertia = 1/12 * self.mass * (3 * (self.size.x / 2) ** 2 + self.size.y ** 2)

        self.drag_type = "cube"

        self.max_thrust = Vector2(0, 7600000)
        self.fuel_consumption = 2500
    
    def get_applied_force(self, application_point, velocity, density):
        return Vector2()
