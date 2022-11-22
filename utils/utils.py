from time import time_ns, perf_counter
from pygame import Vector2


def convert_position(rocket, screen_size, rotated_rocket):
    return screen_size[0] / 2 - rotated_rocket.get_width() / 2, screen_size[1] - rotated_rocket.get_height() - rocket.position.y


def get_time(start_time=0):
    return (time_ns() - start_time) / 1_000_000_000


def _sleep(duration):
    now = perf_counter()
    end = now + duration
    while now < end:
        now = perf_counter()


class Clock:
    def __init__(self, fps=60):
        self.START_TIME = time_ns()
        self.start_time = time_ns()
        self.FPS = fps

    def sleep(self):
        elapsed = time_ns() - self.start_time
        waiting_time = (1_000_000_000 / self.FPS) - elapsed
        if waiting_time > 0:
            _sleep(waiting_time / 1_000_000_000)
        
        self.start_time = time_ns()

    def tick(self):
        now = time_ns()
        delta_t = now - self.start_time
        self.start_time = now

        return delta_t


def intersect_line_line(l1_start, l1_end, l2_start, l2_end):
    if ((l1_start.x == l1_end.x and l1_start.y == l1_end.y) or (l2_start.x == l2_end.x and l2_start.y == l2_end.y)):
        return False

    den = ((l2_end.y - l2_start.y) * (l1_end.x - l1_start.x) - (l2_end.x - l2_start.x) * (l1_end.y - l1_start.y))

    if den == 0:
        return False

    ua = ((l2_end.x - l2_start.x) * (l1_start.y - l2_start.y) - (l2_end.y - l2_start.y) * (l1_start.x - l2_start.x)) / den
    ub = ((l1_end.x - l1_start.x) * (l1_start.y - l2_start.y) - (l1_end.y - l1_start.y) * (l1_start.x - l2_start.x)) / den

    if (ua < 0 or ua > 1 or ub < 0 or ub > 1):
        return False
    
    intersection = Vector2(l1_start.x + ua * (l1_end.x - l1_start.x), l1_start.y + ua * (l1_end.y - l1_start.y))
    if intersection == l1_start or intersection == l1_end or intersection == l2_start or intersection == l2_end:
        return False

    return True