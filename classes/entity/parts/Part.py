from pygame import Vector2, math

from classes.entity.Entity import Entity

from utils.utils import intersect_line_line


class Part(Entity):
    def __init__(self) -> None:
        super().__init__()

        self.name = "Part"

        self.size = Vector2()

        self.sprite = 'None'

        self.starting_points : list[math.Vector2] = []
        self.faces : list[list[math.Vector2]] = []
    
    def get_sprite(self) -> str:
        return self.sprite
    
    def get_application_points(self, velocity : Vector2, rotation : Vector2) -> list[math.Vector2]:
        application_points : list[math.Vector2] = []

        if velocity == Vector2():
            return application_points

        rotated_velocity = velocity.normalize().rotate(Vector2(0, 1).angle_to(rotation))
        rotated_velocity.scale_to_length(2 * self.size.x)
        for starting_point in self.starting_points:
            added = 0
            for face in self.faces:
                if intersect_line_line(starting_point, starting_point + rotated_velocity, face[0], face[1]):
                    added += 1
                    if face[2] not in application_points:
                        application_points.append(face[2])
            if added == 0 and starting_point not in application_points:
                application_points.append(starting_point)
        
        return application_points
    
    def get_applied_force(self, application_point : math.Vector2, velocity : Vector2, rotation : Vector2, density : float) -> Vector2:

        return Vector2()