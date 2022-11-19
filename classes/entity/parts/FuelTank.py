from pygame import Vector2

from classes.entity.parts.Part import Part


class FuelTank(Part):
    def __init__(self):
        super().__init__()

        self.name = "Fuel Tank"
        self.sprite = 'data/parts/fuel_tank.png'

        self.mass = 5018
        self.size = Vector2(4, 12)

        self.drag_type = "long cylinder"

        self.fuel_mass = 120000