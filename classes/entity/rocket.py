from classes.entity.Entity import Entity


class Rocket(Entity):
    def __init__(self, parts):
        super().__init__()
        self.name = "Rocket"

        self.parts = parts