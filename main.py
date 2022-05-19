import pygame
import time

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))

class PID:
    def __init__(self, kp=1, ki=1, kd=1):
        self.__Kp = kp
        self.__Ki = ki
        self.__Kd = kd

        self.__previous_error = 0

    def update(self, error):
        error = -error
        p = error
        i = self.__previous_error + error
        d = error - self.__previous_error
        self.__previous_error = error
        return self.__Kp * p + self.__Ki * i + self.__Kd * d

class Fusee:
    def __init__(self):
        self.fusee = pygame.transform.scale(pygame.image.load('ratio.png').convert_alpha(), (86/5, 638/5))
        self.position = pygame.Vector2(0, 50)
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()

        self.gravity = pygame.Vector2(0, 0.05)
        self.max_thrust = pygame.Vector2(0, -0.1)
        self.drag = pygame.Vector2(0, 0)

        self.thrust = 49
        self.mass = 1

    def update(self):
        if self.velocity == pygame.Vector2():
            self.drag = pygame.Vector2()
        else:
            self.drag = -self.velocity.normalize() * (1/2 * 1.2 * self.velocity.magnitude_squared() * 0.47 * 0.01) / 2

        if self.thrust < 0:
            self.thrust = 0
        elif self.thrust > 100:
            self.thrust = 100

        self.acceleration += self.gravity + self.max_thrust * (self.thrust / 100) + self.drag

        self.velocity += self.acceleration
        self.acceleration = pygame.Vector2()

        self.position += self.velocity

        if self.mass - 0.0005 <= 0:
            self.mass = 0
        else:
            self.mass -= 0.0001


boom = pygame.image.load('boom.png').convert_alpha()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

fusee = Fusee()
pid = PID(.3, 1, 2)

desired_altitude = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                desired_altitude += 5
            if event.key == pygame.K_DOWN:
                desired_altitude -= 5

    screen.fill((0, 0, 0))

    if fusee.position.y > 565:
        screen.blit(boom, (screen.get_width() // 2, screen.get_height() // 2))
        running = False

    fusee.thrust = pid.update(desired_altitude - fusee.position.y)
    fusee.update()

    text_surface = my_font.render(str(fusee.thrust), False, (255, 255, 255))
    text_surface2 = my_font.render(str(desired_altitude) + "  " + str(fusee.position.y), False, (255, 255, 255))
    text_surface3 = my_font.render(str(fusee.mass), False, (255, 255, 255))
    screen.blit(text_surface, (0, 0))
    screen.blit(text_surface2, (0, 30))
    screen.blit(text_surface3, (0, 60))

    screen.blit(fusee.fusee, (screen.get_width() // 2, fusee.position.y))
    pygame.display.update()
    print()
    # time.sleep(0.5)
