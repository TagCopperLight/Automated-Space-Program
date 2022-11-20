from pygame import Vector2

class Entity:
    def __init__(self):
        self.name = ""

        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()

        self.rotation = Vector2(0, 1)
        self.angular_velocity = Vector2()
        self.angular_acceleration = Vector2()

        self.mass = 0
        self.center_of_mass = Vector2()