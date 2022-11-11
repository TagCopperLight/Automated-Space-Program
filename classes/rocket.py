from pygame import transform, image, Vector2
from math import sqrt

from utils.utils import Clock
from utils.physics import get_temperature, get_density, get_gravity_acceleration


class Rocket:
    def __init__(self, x=0, y=75):
        self.rocket = transform.scale(image.load('ratio.png').convert_alpha(), (9, 70))
        self.position = Vector2(x, y)
        self.velocity = Vector2()
        self.acceleration = Vector2()

        self.max_thrust = Vector2(0, 7600000)
        self.drag = Vector2(0, 0)
        self.clock = Clock(60)

        self.thrust = 0
        self.fuel = 1

        self.rocket_mass = 29500
        self.fuel_mass = 488370
        self.total_mass = self.rocket_mass + self.fuel_mass

    def update(self):
        dt = self.clock.tick() / 1_000_000_000

        self.update_physics()

        self.drag = Vector2() if self.velocity == Vector2() else -self.velocity.normalize() * (1/2 * self.density * self.velocity.magnitude_squared() * 0.42 * 3.7)
        self.check_fuel()
        self.total_mass = self.rocket_mass + self.fuel_mass * self.fuel
        self.acceleration = Vector2()

        self.acceleration += (self.gravity * self.total_mass) + self.drag + (self.max_thrust * self.thrust)
        self.acceleration /= (self.total_mass)

        self.velocity += self.acceleration * dt

        self.position += self.velocity * dt

        self.fuel -= 0.006755 * self.thrust * dt

        if self.density != 0:
            self.term_velocity = sqrt((2 * self.total_mass * -self.gravity.y) / (self.density * 0.42 * 3.7))
        else:
            self.term_velocity = 0

    def update_physics(self):
        self.gravity = Vector2(0, -get_gravity_acceleration(self.position.y))
        self.temperature = get_temperature(self.position.y)
        self.density = get_density(self.position.y)

    def check_fuel(self):
        if self.fuel <= 0:
            self.thrust = 0
            self.fuel = 0

    def set_thrust(self, thrust):
        if thrust > 1:
            self.thrust = 1
        elif thrust < 0:
            self.thrust = 0
        else:
            self.thrust = thrust