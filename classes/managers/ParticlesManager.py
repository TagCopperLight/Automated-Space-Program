from pyrticule import particule, shape, maths
from pygame.math import Vector2
from random import uniform, randint
from pygame.surface import Surface
from pygame import SRCALPHA

class ParticlesManager:
    def __init__(self):
        self.fire_group = FireParticleGroup()

    def emit_fire(self, quantity: int = 1):
        self.fire_group.emit(quantity)

    def update(self, delta_t: float):
        self.fire_group.update(delta_t)

    def render(self, delta_t: float):
        return self.fire_group.render(delta_t)
 
class ParticleGroup:
    def __init__(self):
        self.particle_system = particule.ParticleSystem()
        self.particle: particule.Particle
    
    def emit(self, quantity: int = 1):
        for _ in range(quantity):
            self.particle_system.emit(particule.Particle(
            shape = shape.Circle(
                radius = 4,
                angle = randint(0, 10),
                color = (255, 158, 0),
                alpha = 100,
            ),
            position = Vector2(100, 100),
            velocity = Vector2(uniform(-10, 10), uniform(-10, 0)),
            delta_radius = 0.1
        ))

    def update(self, delta_t: float):
        self.particle_system.update(delta_t, Vector2(0, 300))
        
    def render(self, delta_t: float):
        surface = Surface((200, 200), SRCALPHA)

        self.update(delta_t)
        self.particle_system.make_shape()
        self.particle_system.render(surface)

        return surface

class FireParticleGroup(ParticleGroup):
    def __init__(self):
        super().__init__()
        self.particle = particule.Particle(
            shape = shape.Circle(
                radius = 40,
                angle = randint(0, 10),
                color = (255, 158, 0),
                alpha = 100,
            ),
            position = Vector2(100, 100),
            velocity = Vector2(uniform(-10, 10), uniform(-10, 0)),
            delta_radius = 0.1
        )

    def update(self, delta_t: float):
        super().update(delta_t)

        for particle in self.particle_system.particles:
            particle.shape.color = maths.fade_color(particle=particle, color=(235, 0, 0), progress=particle.inverted_progress)
            particle.shape.alpha = maths.fade_alpha(particle=particle, alpha=0, progress=particle.inverted_progress)
