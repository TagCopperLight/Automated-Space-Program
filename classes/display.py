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
            thrust_text = self.FONT.render(f'{rocket.thrust * 100:.3f}', False, Colors.WHITE.value)
            altitude_text = self.FONT.render(f'{rocket.velocity.y:.3f}' + "  " + f'{rocket.position.y:.3f}', False, Colors.WHITE.value)
            fuel_text = self.FONT.render(f'{rocket.fuel * 100:.3f}', False, Colors.WHITE.value)
            surface.blit(thrust_text, (10, 10))
            surface.blit(altitude_text, (10, 40))
            surface.blit(fuel_text, (10, 70))
        
        ground = Rect(*convert_position((0, 75), screen_size), screen_size[0], 150)
        draw.rect(surface, Colors.GROUND.value, ground)

        surface.blit(rocket.rocket, convert_position(rocket.position + Vector2(0, rocket.rocket.get_height()), screen_size))
        
        return surface