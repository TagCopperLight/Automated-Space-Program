from time import time_ns
from utils.utils import get_time

import mysql.connector
import socket
import json


class Logger:
    def __init__(self):
        self.START_TIME = time_ns()
    
    def send_data_udp(self, rocket):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('127.0.0.1', 4000))

        data = {
            "type": "data",
            "data": {
                "altitude": {
                    "time": get_time(self.START_TIME),
                    "altitude": rocket.position.y
                },
                "velocity": {
                    "time": get_time(self.START_TIME),
                    "velocity": rocket.velocity.y
                },
                "trust": {
                    "time": get_time(self.START_TIME),
                    "trust": rocket.thrust * 100
                },
                "fuel": {
                    "time": get_time(self.START_TIME),
                    "fuel": rocket.fuel / rocket.fuel_mass
                }
            }
        }

        sock.sendall(json.dumps(data).encode('utf-8'))

        sock.close()

    def database_init(self):
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "tag",
            password = "",
            database = "RocketSimulator"
        )

        cursor = self.db.cursor()

        sql = "TRUNCATE altitude"
        cursor.execute(sql)
        self.db.commit()
    
    def send_data(self, rocket):
        cursor = self.db.cursor()

        sql = "INSERT INTO altitude (t, altitude) VALUES (%s, %s)"
        values = (get_time(self.START_TIME), rocket.position.y)

        cursor.execute(sql, values)

        self.db.commit()