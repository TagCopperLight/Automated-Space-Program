from pygame import Vector2

from classes.entity.parts.Part import Part


class Engine(Part):
    def __init__(self):
        super().__init__()

        self.name = "Engine"
        self.sprite = 'data/parts/engine.png'

        self.mass = 4410
        self.size = Vector2(4, 4)

        self.drag_type = "cube"

        self.max_thrust = Vector2(0, 7600000)
        self.fuel_consumption = 2500