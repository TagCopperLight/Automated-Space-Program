from classes.entity.parts.Part import Part


class Fairing(Part):
    def __init__(self):
        super().__init__()

        self.name = "Fairing"
        self.sprite = 'data/parts/fairing.png'

        self.mass = 5018
        self.size = (4, 12)

        self.drag_type = "ogive" # Cd = 0.23