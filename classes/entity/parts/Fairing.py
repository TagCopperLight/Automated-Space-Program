from pygame import Vector2

from classes.entity.parts.Part import Part


class Fairing(Part):
    def __init__(self ) -> None:
        super().__init__()

        self.name = "Fairing"
        self.sprite = 'data/parts/fairing.png'

        self.mass = 5018
        self.size = Vector2(4, 12)

        self.starting_points = [
            self.position,
            self.position + self.size / 2,
            self.position + Vector2(0, self.size.y),
            self.position + Vector2(-self.size.x / 2, self.size.y / 2)
            ]
        self.faces = [
            #[self.position + Vector2(-self.size.x / 2, 0), self.position + Vector2(self.size.x / 2, 0), self.position],
            [self.position + Vector2(self.size.x / 2, 0), self.position + Vector2(self.size.x / 2, self.size.y), self.position + self.size / 2],
            [self.position + Vector2(self.size.x / 2, self.size.y), self.position + Vector2(-self.size.x / 2, self.size.y), self.position + Vector2(0, self.size.y)],
            [self.position + Vector2(-self.size.x / 2, self.size.y), self.position + Vector2(-self.size.x / 2, 0), self.position + Vector2(-self.size.x / 2, self.size.y / 2)]
            ]

        self.moment_of_inertia = self.mass * (3/20 * (self.size.x / 2) ** 2 + 3/80 * self.size.y ** 2)

        self.drag_type = "cone"