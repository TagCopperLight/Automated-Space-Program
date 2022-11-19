from classes.entity.parts.Part import Part


class Motor(Part):
    def __init__(self, max_thrust, fuel_comsumption):
        super().__init__()

        self.name = "Motor"
        self.sprite = 'data/parts/motor.png'

        self.mass = 4410
        self.size = (4, 4)

        self.drag_type = "cube"

        self.max_thrust = max_thrust
        self.fuel_consumption = fuel_comsumption