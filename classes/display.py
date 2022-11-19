from pygame import font, Surface, Rect, draw, SRCALPHA, Vector2, transform

from utils.colors import Colors
from utils.utils import convert_position


class Display:
    def __init__(self, debug=False):
        self.debug = debug
        self.FONT = font.SysFont('Comic Sans MS', 20)

    def update(self, screen_size, rocket):
        surface = Surface(screen_size, SRCALPHA)

        if self.debug:
            velocity_text = self.FONT.render(f'Velocity : {rocket.velocity.y:.3f} m/s', True, Colors.BLACK.value)
            position_text = self.FONT.render(f'Altitude : {rocket.position.y:.3f} m', True, Colors.BLACK.value)
            term_vel_text = self.FONT.render(f'Terminal velocity : {rocket.term_velocity:.3f} m/s', True, Colors.BLACK.value)
            thrust_text = self.FONT.render(f'Thrust : {rocket.thrust * 100:.3f} %', True, Colors.BLACK.value)
            fuel_text = self.FONT.render(f'Fuel : {rocket.fuel / rocket.fuel_mass * 100:.3f} %', True, Colors.BLACK.value)
            mass_text = self.FONT.render(f'Mass : {rocket.mass:.3f} kg', True, Colors.BLACK.value)
            surface.blit(velocity_text, (10, 10))
            surface.blit(position_text, (10, 40))
            surface.blit(term_vel_text, (10, 70))
            surface.blit(thrust_text, (10, 100))
            surface.blit(fuel_text, (10, 130))
            surface.blit(mass_text, (10, 160))
        
        ground = Rect(0, 675, screen_size[0], 150)
        draw.rect(surface, Colors.GROUND.value, ground)

        rotated_rocket = transform.rotate(rocket.rocket, rocket.rotation.angle_to(Vector2(0, 1)))

        pos_to_show = convert_position(rocket, screen_size, rotated_rocket)

        surface.blit(rotated_rocket, pos_to_show)
        
        return surface