import numpy as np
import matplotlib.pyplot as plt
from pygame import Vector2

from utils.constants import Constants


def get_temperature(h):
    for index, alt in enumerate(Constants.ALTITUDE_X.value):
        if index == len(Constants.ALTITUDE_X.value) - 1:
            return Constants.TEMPERATURE_Y.value[index]

        if alt <= h < Constants.ALTITUDE_X.value[index + 1]:
            lower = Vector2(Constants.ALTITUDE_X.value[index], Constants.TEMPERATURE_Y.value[index])
            upper = Vector2(Constants.ALTITUDE_X.value[index + 1], Constants.TEMPERATURE_Y.value[index + 1])

            return lower.lerp(upper, (h - lower.x) / (upper.x - lower.x)).y

def get_density(h):
    for index, alt in enumerate(Constants.ALTITUDE_X.value):
        if index == len(Constants.ALTITUDE_X.value) - 1:
            return Constants.DENSITY_Y.value[index]

        if alt <= h < Constants.ALTITUDE_X.value[index + 1]:
            lower = Vector2(Constants.ALTITUDE_X.value[index], Constants.DENSITY_Y.value[index])
            upper = Vector2(Constants.ALTITUDE_X.value[index + 1], Constants.DENSITY_Y.value[index + 1])

            return lower.lerp(upper, (h - lower.x) / (upper.x - lower.x)).y

def get_gravity_acceleration(h):
    return Constants.ACCEL_GRAVITY_AT_0.value * (Constants.MEAN_RADIUS_EARTH.value / (Constants.MEAN_RADIUS_EARTH.value + h)) ** 2
    