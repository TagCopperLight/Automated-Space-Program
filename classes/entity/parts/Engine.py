from pygame import Vector2

from classes.entity.parts.Part import Part


class Engine(Part):
    def __init__(self):
        super().__init__()

        self.name = "Engine"
        self.sprite = 'data/parts/engine.png'

        self.mass = 4410
        self.size = Vector2(4, 4)
        
        self.moment_of_inertia = 1/12 * self.mass * (3 * (self.size.x / 2) ** 2 + self.size.y ** 2)

        self.drag_type = "cube"

        self.max_thrust = Vector2(0, 7600000)
        self.fuel_consumption = 2500
    
    def get_application_points(self, rotation):
        return [
            self.position.copy(),
            Vector2(self.position.x + self.size.x / 2, self.position.y + self.size.y / 2),
            Vector2(self.position.x - self.size.x / 2, self.position.y + self.size.y / 2),
            Vector2(self.position.x + self.size.x, self.position.y),
                ]
    
    def get_applied_force(self, application_point, velocity, density):
        return Vector2()

