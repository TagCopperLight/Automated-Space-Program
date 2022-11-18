from time import time_ns
from utils.utils import get_time

import socket
import json


class Logger:
    def __init__(self):
        self.START_TIME = time_ns()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 4000))
        self.sock.sendall(json.dumps({"type": "reset"}).encode('utf-8'))
    
    def send_data_tcp(self, rocket):
        data = {
            "type": "data",
            "data_type": [
                "altitude",
                "velocity",
                "thrust",
                "fuel"
            ],
            "data": {
                "altitude": {
                    "time": round(get_time(self.START_TIME), 2),
                    "altitude": rocket.position.y
                },
                "velocity": {
                    "time": round(get_time(self.START_TIME), 2),
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

        self.sock.sendall(json.dumps(data).encode('utf-8'))