import numpy as np
import matplotlib.pyplot as plt
from pygame import Vector2


ALTITUDE_X = [1000 * i for i in range(11)] + [15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]

TEMPERATURE_Y = [15, 8.5, 2, -4.49, -10.98, -17.47, -23.96, -30.45, -36.94, -43.42, -49.9, -56.5, -56.5, -51.6, -46.64, -22.8, -2.5, -26.13, -53.57, -74.51, -87]


def get_temperature(h):
    for index, alt in enumerate(ALTITUDE_X):
        if index == len(ALTITUDE_X) - 1:
            return TEMPERATURE_Y[index]

        if alt <= h < ALTITUDE_X[index + 1]:
            lower = Vector2(ALTITUDE_X[index], TEMPERATURE_Y[index])
            upper = Vector2(ALTITUDE_X[index + 1], TEMPERATURE_Y[index + 1])

            return lower.lerp(upper, (h - lower.x) / (upper.x - lower.x)).y