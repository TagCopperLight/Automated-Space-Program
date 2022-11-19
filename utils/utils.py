from time import time_ns, perf_counter


def convert_position(rocket, screen_size, rotated_rocket):
    return screen_size[0] / 2 - rotated_rocket.get_width() / 2, screen_size[1] - rocket.rocket.get_height()/2 - rotated_rocket.get_height() / 2 - rocket.position.y


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