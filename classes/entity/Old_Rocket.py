from pygame import transform, image, Vector2, K_z, K_s, K_LEFT, K_RIGHT
from math import sqrt, pi

from classes.entity.Entity import Entity

from utils.utils import Clock
from utils.physics import get_temperature, get_density, get_gravity_acceleration
from utils.constants import Constants


class Rocket(Entity):
    def __init__(self):
        super().__init__()

        self.name = "Rocket"
        
        self.rocket = transform.scale(image.load('data/ratio.png').convert_alpha(), (4, 65))

        self.max_thrust = Vector2(0, 7600000)
        self.drag = Vector2(0, 0)
        self.clock = Clock(60)

        self.thrust = 0

        self.rocket_mass = 29500
        self.fuel_mass = 480000
        self.fuel = self.fuel_mass
        self.mass = self.rocket_mass + self.fuel_mass
        self.fuel_consumption = 2500

    def update(self, events):
        dt = self.clock.tick() / 1_000_000_000

        self.player_update(events)

        self.update_physics()

        self.drag = Vector2() if self.velocity == Vector2() else -self.velocity.normalize() * (1/2 * self.density * self.velocity.magnitude_squared() * 0.42 * 0.25)
        self.check_fuel()
        self.acceleration = Vector2()

        self.acceleration += (self.gravity * self.mass) + self.drag + (self.max_thrust * self.thrust)
        self.acceleration /= (self.mass)

        self.velocity += self.acceleration * dt

        self.check_velocity()

        self.position += self.velocity * dt

        self.check_position()

        self.fuel -= self.fuel_consumption * self.thrust * dt

        if self.density != 0:
            self.term_velocity = sqrt((2 * self.mass * -self.gravity.y) / (self.density * 0.42 * 0.25))
        else:
            self.term_velocity = 0

    def update_physics(self):
        self.gravity = Vector2(0, -get_gravity_acceleration(self.position.y))
        self.temperature = get_temperature(self.position.y)
        self.density = get_density(self.position.y)

        self.mass = (self.rocket_mass + self.fuel) / sqrt(1 - (self.velocity.y / Constants.LIGHT_SPEED.value) ** 2)

    def player_update(self, events):
        for event in events.keys_down:
            if event == K_z:
                self.set_thrust(self.thrust + 0.1)
            elif event == K_s:
                self.set_thrust(self.thrust - 0.1)
            elif event == K_LEFT:
                self.rotation.rotate_ip_rad(-pi/10)
            elif event == K_RIGHT:
                self.rotation.rotate_ip_rad(pi/10)

    def check_fuel(self):
        if self.fuel <= 0:
            self.thrust = 0
            self.fuel = 0

    def check_velocity(self):
        if self.velocity.y >= Constants.LIGHT_SPEED.value:
            self.velocity.y = Constants.LIGHT_SPEED.value - .000001
    
    def check_position(self):
        if self.position.y <= 60:
            self.position.y = 60
            self.velocity = Vector2()

    def set_thrust(self, thrust):
        if thrust > 1:
            self.thrust = 1
        elif thrust < 0:
            self.thrust = 0
        else:
            self.thrust = thrust