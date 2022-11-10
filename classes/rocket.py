from pygame import transform, image, Vector2


class Rocket:
    def __init__(self, x=0, y=75):
        self.rocket = transform.scale(image.load('ratio.png').convert_alpha(), (86/5, 638/5))
        self.position = Vector2(x, y)
        self.velocity = Vector2()
        self.acceleration = Vector2()

        self.gravity = Vector2(0, -9.81)
        self.max_thrust = Vector2(0, 20)
        self.drag = Vector2(0, 0)

        self.thrust = 0
        self.fuel = 1

        self.rocket_mass = 5000
        self.fuel_mass = 5000
        self.total_mass = self.rocket_mass + self.fuel_mass

    def update(self, delta_t):
        #self.drag = Vector2() if self.velocity == Vector2() else -self.velocity.normalize() * (1/2 * 1.2 * self.velocity.magnitude_squared() * 0.47 * 0.01) / 2
        self.check_fuel()
        self.total_mass = self.rocket_mass + self.fuel_mass * self.fuel
        self.acceleration = Vector2()

        self.acceleration += (self.gravity * self.total_mass) + self.drag + (self.max_thrust * self.thrust)
        self.acceleration /= (self.total_mass)

        self.velocity += self.acceleration * delta_t

        self.position += self.velocity * delta_t

        #self.fuel -= 0.0005 * self.thrust

    def check_fuel(self):
        if self.fuel <= 0:
            self.thrust = 0
            self.fuel = 0

    def set_thrust(self, thrust):
        if thrust > 100:
            thrust = 100
        elif thrust < 0:
            thrust = 0
        
        self.thrust = thrust