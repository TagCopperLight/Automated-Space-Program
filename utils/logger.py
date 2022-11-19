from time import time_ns
from utils.utils import get_time

import socket
import json


class Logger:
    def __init__(self):
        self.START_TIME = time_ns()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 4000))
        self.sock.sendall((json.dumps({"type": "reset"}) + 'eof').encode('utf-8'))
    
    def send_data_tcp(self, rocket):
        data = {
            "type": "data",
            "data_type": [
                "altitude",
                "velocity",
                "acceleration",
                "drag"
            ],
            "colors": {
                "altitude": "#b4befe",
                "velocity": "#f9e2af",
                "acceleration": "#fab387",
                "drag": "#f38ba8"
            },
            "data": {
                "altitude": {
                    "time": get_time(self.START_TIME),
                    "altitude": rocket.position.y
                },
                "velocity": {
                    "time": get_time(self.START_TIME),
                    "velocity": rocket.velocity.y
                },
                "acceleration": {
                    "time": get_time(self.START_TIME),
                    "acceleration": rocket.acceleration.y
                },
                "drag": {
                    "time": get_time(self.START_TIME),
                    "drag": rocket.drag.y
                }
            }
        }
        self.sock.sendall((json.dumps(data) + 'eof').encode('utf-8'))