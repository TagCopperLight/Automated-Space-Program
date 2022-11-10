from time import time_ns


def convert_position(position, screen_size):
    return position[0], screen_size[1] - position[1]


def get_time(start_time=0):
    return (time_ns() - start_time) / 1_000_000_000