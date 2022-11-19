from pygame import Vector2


class PartsManager:
    def __init__(self, parts):
        self.parts = parts
    
    def get_total_rocket_mass(self):
        total_mass = 0
        for part in self.parts:
            total_mass += part.mass
        return total_mass
    
    def get_total_fuel_mass(self):
        total_mass = 0
        for part in self.parts:
            if part.name == "Fuel Tank":
                total_mass += part.fuel_mass
        return total_mass
    
    def get_total_fuel_comsumption(self):
        total_fuel_consumption = 0
        for part in self.parts:
            if part.name == "Engine":
                total_fuel_consumption += part.fuel_consumption
        return total_fuel_consumption
    
    def get_total_thrust(self) -> Vector2:
        total_thrust = Vector2()
        for part in self.parts:
            if part.name == "Engine":
                total_thrust += part.max_thrust
        return total_thrust

# ------------------------------ Rotations ------------------------------ #
    
    def update_positions(self):
        current_pos = Vector2()
        for part in self.parts:
            part.position = current_pos.copy()
            current_pos += Vector2(0, part.size.y)

    def get_center_of_mass(self) -> Vector2:
        center_of_mass = Vector2()
        for part in self.parts:
            if part.name == "Fuel Tank":
                center_of_mass += part.position * (part.mass + part.fuel_mass)
            else:
                center_of_mass += part.position * part.mass
        center_of_mass /= self.get_total_rocket_mass() + self.get_total_fuel_mass()

        return center_of_mass