from pygame import font, Surface, Rect, draw, SRCALPHA, Vector2

from classes.colors import Colors
from utils.utils import convert_position


class Display:
    def __init__(self, debug=False):
        self.debug = debug
        self.FONT = font.SysFont('Comic Sans MS', 30)

    def update(self, screen_size, rocket, desired_altitude):
        surface = Surface(screen_size, SRCALPHA)

        if self.debug:
            velocity_text = self.FONT.render(f'Velocity : {rocket.velocity.y:.3f} m/s', False, Colors.WHITE.value)
            position_text = self.FONT.render(f'Altitude : {rocket.position.y:.3f} m', False, Colors.WHITE.value)
            term_vel_text = self.FONT.render(f'Terminal velocity : {rocket.term_velocity:.3f} m/s', False, Colors.WHITE.value)
            thrust_text = self.FONT.render(f'Thrust : {rocket.thrust * 100:.3f} %', False, Colors.WHITE.value)
            fuel_text = self.FONT.render(f'Fuel : {rocket.fuel * 100:.3f} %', False, Colors.WHITE.value)
            surface.blit(velocity_text, (10, 10))
            surface.blit(position_text, (10, 40))
            surface.blit(term_vel_text, (10, 70))
            surface.blit(thrust_text, (10, 100))
            surface.blit(fuel_text, (10, 130))
        
        ground = Rect(*convert_position((0, 75), screen_size), screen_size[0], 150)
        draw.rect(surface, Colors.GROUND.value, ground)

        surface.blit(rocket.rocket, convert_position(rocket.position + Vector2(0, rocket.rocket.get_height()), screen_size))
        
        return surface