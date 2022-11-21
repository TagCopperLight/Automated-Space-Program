from pygame import Vector2, K_z, K_q, K_s, K_d, transform, image
from math import sqrt, pi

from classes.entity.Entity import Entity
from classes.managers.PartsManager import PartsManager

from utils.utils import Clock
from utils.physics import get_temperature, get_density, get_gravity_acceleration
from utils.constants import Constants


class Rocket(Entity):
    def __init__(self, parts):
        super().__init__()

        self.name = "Rocket"

        self.rocket = transform.scale(image.load('data/ratio.png').convert_alpha(), (4, 65))

        self.parts = parts
        self.parts_manager = PartsManager(self.parts)
        self.parts_manager.update_positions()
        self.center_of_mass = self.parts_manager.get_center_of_mass()

        self.max_thrust = self.parts_manager.get_total_thrust()
        self.thrust = 0

        self.drag = Vector2()
        self.clock = Clock()

        self.rocket_mass = self.parts_manager.get_total_rocket_mass()
        self.fuel_mass = self.parts_manager.get_total_fuel_mass()
        self.fuel = self.fuel_mass
        self.mass = self.rocket_mass + self.fuel_mass

        self.fuel_consumption = self.parts_manager.get_total_fuel_comsumption()

        self.gravity = Vector2()
        self.temperature = 0
        self.density = 0

        self.terminal_velocity = 0
    
    def update(self, events):
        dt = self.clock.tick() / 1_000_000_000

        self.update_from_player(events)

        self.check_fuel()

        self.update_physics()

        self.update_translations(dt)

        #self.update_rotations(dt)

        self.set_fuel(dt)
    
    def update_from_player(self, events):
        for event in events.keys_down:
            if event == K_z:
                self.set_thrust(self.thrust + 0.1)
            elif event == K_s:
                self.set_thrust(self.thrust - 0.1)
            elif event == K_q:
                self.max_thrust.rotate_ip_rad(-pi/12)
            elif event == K_d:
                self.max_thrust.rotate_ip_rad(pi/12)
    
    def check_fuel(self):
        if self.fuel <= 0:
            self.thrust = 0
            self.fuel = 0
    
    def check_position(self):
        if self.position.y <= 60:
            self.position.y = 60
            self.velocity = Vector2()
    
    def update_physics(self):
        self.gravity = Vector2(0, -get_gravity_acceleration(self.position.y))
        self.temperature = get_temperature(self.position.y)
        self.density = get_density(self.position.y)

        self.mass = (self.rocket_mass + self.fuel) / sqrt(1 - (self.velocity.y / Constants.LIGHT_SPEED.value) ** 2)
        
        self.terminal_velocity = sqrt((2 * self.mass * -self.gravity.y) / (self.density * 0.42 * 0.25)) if self.density != 0 else 0
        self.drag = Vector2() if self.velocity == Vector2() else -self.velocity.normalize() * (1/2 * self.density * self.velocity.magnitude_squared() * 0.42 * 0.25)

    def update_translations(self, dt):
        self.acceleration = Vector2()

        self.acceleration += (self.gravity * self.mass) + self.drag + (self.max_thrust * self.thrust)
        self.acceleration /= (self.mass)

        self.velocity += self.acceleration * dt

        self.position += self.velocity * dt

        self.check_position()

    def update_rotations(self, dt):
        self.angular_acceleration = self.parts_manager.get_total_angular_acceleration(self.velocity, self.density, self.rotation)

        self.angular_velocity += self.angular_acceleration * dt

        print(self.angular_velocity)
    
    def set_thrust(self, thrust):
        self.thrust = max(min(thrust, 1), 0)

    def set_fuel(self, dt):
        self.fuel -= self.fuel_consumption * self.thrust * dt