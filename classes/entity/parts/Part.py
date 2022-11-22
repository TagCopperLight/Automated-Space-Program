from pygame import Vector2

from classes.entity.Entity import Entity

from utils.utils import intersect_line_line


class Part(Entity):
    def __init__(self):
        super().__init__()

        self.name = "Part"

        self.size = Vector2()

        self.sprite = None

        self.starting_points = []
        self.faces = []
    
    def get_sprite(self):
        return self.sprite
    
    def get_application_points(self, velocity : Vector2, rotation):
        application_points = []

        if velocity == Vector2():
            return application_points

        rotated_velocity = velocity.normalize().rotate(Vector2(0, 1).angle_to(rotation))
        rotated_velocity.scale_to_length(2 * self.size.x)
        for starting_point in self.starting_points:
            for face in self.faces:
                if intersect_line_line(starting_point, starting_point + rotated_velocity, face[0], face[1]):
                    if face[2] not in application_points:
                        application_points.append(face[2])
                else:
                    if starting_point not in application_points:
                        application_points.append(starting_point)
        
        print(f'{self.name} : {application_points}')

        return application_points
    
    def get_applied_force(self, application_point, velocity, density):
        return Vector2()