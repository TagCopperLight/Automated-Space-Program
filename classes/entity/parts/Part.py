from classes.entity.Entity import Entity


class Part(Entity):
    def __init__(self):
        super().__init__()

        self.name = "Part"

        self.sprite = None
    
    def get_sprite(self):
        return self.sprite