from pygame import font, Surface, Rect, draw, SRCALPHA, Vector2, transform, math

from classes.entity.Entity import Entity
from classes.managers.ParticlesManager import ParticlesManager

from utils.colors import Colors
from utils.utils import convert_position


class DisplayManager:
    def __init__(self, debug : bool = False) -> None:
        self.debug = debug
        self.FONT = font.Font('data/Roboto-Bold.ttf', 20)
        self.debug_vectors: list[tuple[math.Vector2, math.Vector2, tuple[int, int, int]]] = []

        self.particles_manager = ParticlesManager()

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
                rocket_image : Surface = entity.parts_manager.get_full_sprite() #type: ignore
                rotated_rocket = transform.rotate(rocket_image, entity.rotation.angle_to(Vector2(0, 1)))
                pos_to_show = convert_position(entity.position, screen_size, rocket_image, rotated_rocket)
                
                s = Surface((0, rocket_image.get_height() / 2))
                
                self.particles_manager.emit_fire(10)
                particle_surface = self.particles_manager.render(1/60)
                surface.blit(particle_surface, convert_position(entity.position + Vector2(0, -32) + Vector2(100, 100), screen_size, s, s)) #type: ignore

                surface.blit(rotated_rocket, pos_to_show)

                for vector in self.debug_vectors:
                    self.draw_vector(surface, -vector[0], vector[2], convert_position(Vector2(vector[1].x, vector[1].y), screen_size, s, s))
                
                self.debug_vectors = []

                
        return surface
    
    def draw_debug(self, surface : Surface, entity : Entity) -> None:
        surface.blit(self.FONT.render(f'Velocity : {entity.velocity.y:.3f} m/s', True, Colors.BLACK.value), (10, 10))
        surface.blit(self.FONT.render(f'Altitude : {entity.position.y:.3f} m', True, Colors.BLACK.value), (10, 40))
        surface.blit(self.FONT.render(f'Terminal velocity : {entity.terminal_velocity:.3f} m/s', True, Colors.BLACK.value), (10, 70)) #type: ignore
        surface.blit(self.FONT.render(f'Thrust : {entity.thrust * 100:.3f} %', True, Colors.BLACK.value), (10, 100)) #type: ignore
        surface.blit(self.FONT.render(f'Fuel : {entity.fuel / entity.fuel_mass * 100:.3f} %', True, Colors.BLACK.value), (10, 130)) #type: ignore

    def draw_vector(self, surface : Surface, vector : math.Vector2, color : tuple[int, int, int], position : math.Vector2) -> None:
        draw.line(surface, color, position, position + vector, 3)