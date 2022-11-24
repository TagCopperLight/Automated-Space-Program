from pygame import font, Surface, Rect, draw, SRCALPHA, Vector2, transform

from classes.entity.Entity import Entity

from utils.colors import Colors
from utils.utils import convert_position


class DisplayManager:
    def __init__(self, debug : bool = False) -> None:
        self.debug = debug
        self.FONT = font.Font('data/Roboto-Bold.ttf', 20)

    def update(self, screen_size : tuple[int, int], entities : list[Entity]) -> Surface:
        surface = Surface(screen_size, SRCALPHA)

        surface.fill(Colors.SKY.value)

        if self.debug:
            for entity in entities:
                if entity.name == 'Rocket':
                    self.draw_debug(surface, entity)
        
        ground = Rect(0, screen_size[1] - 60, screen_size[0], 150)
        draw.rect(surface, Colors.GROUND.value, ground)

        for entity in entities:
            if entity.name == 'Rocket':
                rotated_rocket = transform.rotate(entity.parts_manager.get_full_sprite(), entity.rotation.angle_to(Vector2(0, 1)))

                pos_to_show = convert_position(entity, screen_size, rotated_rocket)

                surface.blit(rotated_rocket, pos_to_show)
                
        return surface
    
    def draw_debug(self, surface : Surface, entity : Entity) -> None:
        surface.blit(self.FONT.render(f'Velocity : {entity.velocity.y:.3f} m/s', True, Colors.BLACK.value), (10, 10))
        surface.blit(self.FONT.render(f'Altitude : {entity.position.y:.3f} m', True, Colors.BLACK.value), (10, 40))
        surface.blit(self.FONT.render(f'Terminal velocity : {entity.terminal_velocity:.3f} m/s', True, Colors.BLACK.value), (10, 70)) #type: ignore
        surface.blit(self.FONT.render(f'Thrust : {entity.thrust * 100:.3f} %', True, Colors.BLACK.value), (10, 100)) #type: ignore
        surface.blit(self.FONT.render(f'Fuel : {entity.fuel / entity.fuel_mass * 100:.3f} %', True, Colors.BLACK.value), (10, 130)) #type: ignore