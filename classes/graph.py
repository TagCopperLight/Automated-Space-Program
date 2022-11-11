from time import time_ns
import matplotlib.pyplot as plt
from utils.utils import get_time

class Graph:
    def __init__(self):
        self.START_TIME = time_ns()

        self.x_pos, self.y_pos = [], []
        self.x_vel, self.y_vel = [], []
        self.x_accel, self.y_accel = [], []
        self.x_thrust, self.y_thrust = [], []

    def update(self, rocket):
        self.x_pos.append(get_time(self.START_TIME))
        self.y_pos.append(rocket.position.y)

        self.x_vel.append(get_time(self.START_TIME))
        self.y_vel.append(rocket.velocity.y)

        self.x_accel.append(get_time(self.START_TIME))
        self.y_accel.append(rocket.acceleration.y)

        self.x_thrust.append(get_time(self.START_TIME))
        self.y_thrust.append(rocket.thrust * 100)

    def show(self):
        plt.plot(self.x_pos, self.y_pos, 'red')
        plt.plot(self.x_vel, self.y_vel, 'orange')
        plt.plot(self.x_accel, self.y_accel, 'yellow')
        plt.plot(self.x_thrust, self.y_thrust, 'green')

        plt.show()
