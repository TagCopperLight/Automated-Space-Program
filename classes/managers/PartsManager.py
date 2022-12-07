from pygame import Vector2, math, image, transform, Surface, SRCALPHA

from classes.entity.parts.Part import Part
from classes.managers.DisplayManager import DisplayManager


class PartsManager:
    def __init__(self, parts : list[Part], display_manager : DisplayManager) -> None:
        self.parts = parts
        self.display_manager = display_manager
    
    def get_total_rocket_mass(self) -> float:
        total_mass = 0
        for part in self.parts:
            total_mass += part.mass
        return total_mass
    
    def get_total_fuel_mass(self) -> float:
        total_mass : float = 0
        for part in self.parts:
            if part.name == "Fuel Tank":
                total_mass += part.fuel_mass # type: ignore
        return total_mass
    
    def get_total_fuel_comsumption(self) -> float:
        total_fuel_consumption : float = 0
        for part in self.parts:
            if part.name == "Engine":
                total_fuel_consumption += part.fuel_consumption # type: ignore
        return total_fuel_consumption
    
    def get_total_thrust(self) -> Vector2:
        total_thrust : Vector2 = Vector2()
        for part in self.parts:
            if part.name == "Engine":
                total_thrust += part.max_thrust # type: ignore
        return total_thrust
    
    def get_total_moment_of_inertia(self) -> float:
        total_moment_of_inertia : float = 0

        for part in self.parts:
            total_moment_of_inertia += part.moment_of_inertia # type: ignore
        
        return total_moment_of_inertia

# ------------------------------- Sprites ------------------------------- #

    def get_full_sprite(self, n : int = 1) -> Surface:
        full_sprite_surface = Surface((0, 0), SRCALPHA)
        for part in self.parts:
            sprite = transform.scale(image.load(part.sprite), part.size * n)

            if full_sprite_surface.get_width() < part.size.x * n:
                last_surface = full_sprite_surface.copy()
                full_sprite_surface = Surface((part.size.x * n, full_sprite_surface.get_height()), SRCALPHA)
                full_sprite_surface.blit(last_surface, ((full_sprite_surface.get_width() - last_surface.get_width()) // 2, full_sprite_surface.get_height() - last_surface.get_height()))

            if full_sprite_surface.get_height() < full_sprite_surface.get_height() + part.size.y * n:
                last_surface = full_sprite_surface.copy()
                full_sprite_surface = Surface((full_sprite_surface.get_width(), full_sprite_surface.get_height() + part.size.y * n), SRCALPHA)
                full_sprite_surface.blit(last_surface, ((full_sprite_surface.get_width() - last_surface.get_width()) // 2, full_sprite_surface.get_height() - last_surface.get_height()))

            full_sprite_surface.blit(sprite, (full_sprite_surface.get_width() // 2 - part.size.x * n // 2 + part.position.x * n, full_sprite_surface.get_height() - part.position.y * n - part.size.y * n))

        return full_sprite_surface

# ------------------------------ Rotations ------------------------------ #
    
    def update_positions(self) -> None:
        current_pos = Vector2()
        for part in self.parts:
            part.position = current_pos.copy() # type: ignore
            part.center_of_mass = part.position + Vector2(0, part.size.y / 2) # type: ignore
            current_pos += Vector2(0, part.size.y)

    def get_center_of_mass(self) -> Vector2:
        center_of_mass : Vector2 = Vector2()
        for part in self.parts:
            if part.name == "Fuel Tank":
                center_of_mass += part.center_of_mass * (part.mass + part.fuel_mass) # type: ignore
            else:
                center_of_mass += part.center_of_mass * part.mass # type: ignore
        center_of_mass /= self.get_total_rocket_mass() + self.get_total_fuel_mass() # type: ignore

        return center_of_mass
    
    def get_total_angular_acceleration(self, position : Vector2, velocity : Vector2, density : float, rotation : Vector2) -> math.Vector2:
        total_angular_acceleration = Vector2()
        center_of_mass = self.get_center_of_mass()
        moment_of_inertia = self.get_total_moment_of_inertia()
        total_vectors = 1

        for part in self.parts:
            for application_point in part.get_application_points(velocity, rotation):
                applied_force = part.get_applied_force(application_point, velocity, rotation, density)

                moment_arm = application_point - center_of_mass

                parallel_component = applied_force.dot(moment_arm) / moment_arm.length_squared() * moment_arm
                angular_force = applied_force - parallel_component

                torque = angular_force * moment_arm.length()

                self.display_manager.debug_vectors.append((torque / moment_of_inertia * 10, part.position + position + Vector2(0, -32), (255, 0, 0)))

                total_angular_acceleration += torque
                total_vectors += 1

        return total_angular_acceleration / moment_of_inertia / total_vectors