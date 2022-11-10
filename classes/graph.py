from time import time_ns
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.START_TIME = time_ns()

        self.x_pos, self.y_pos = [], []
        self.x_desired, self.y_desired = [], []
        self.x_thrust, self.y_thrust = [], []
        self.x_accel, self.y_accel = [], []

    def update(self, rocket, desired_altitude):
        self.x_pos.append(time_ns() - self.START_TIME)
        self.y_pos.append(rocket.position.y)

        self.x_desired.append(time_ns() - self.START_TIME)
        self.y_desired.append(desired_altitude)

        self.x_thrust.append(time_ns() - self.START_TIME)
        self.y_thrust.append(rocket.thrust * 100)

        self.x_accel.append(time_ns() - self.START_TIME)
        self.y_accel.append(rocket.velocity.y)

    def show(self):
        plt.plot(self.x_pos, self.y_pos, 'r')
        plt.plot(self.x_desired, self.y_desired, 'g')
        plt.plot(self.x_thrust, self.y_thrust, 'orange')
        plt.plot(self.x_accel, self.y_accel, 'yellow')

        plt.show()