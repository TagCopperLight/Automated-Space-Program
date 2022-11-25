from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classes.entity.Rocket import Rocket

from time import time_ns
from socket import socket, AF_INET, SOCK_STREAM
from json import dumps

from utils.utils import get_time



class Logger:
    def __init__(self, activate : bool = True) -> None:
        self.START_TIME = time_ns()
        self.activate = activate

        if activate:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(('127.0.0.1', 4000))
            self.sock.sendall((dumps({"type": "reset"}) + 'eof').encode('utf-8'))
    
    def send_data_tcp(self, rocket : 'Rocket') -> None:
        if not self.activate:
            return None
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
        self.sock.sendall((dumps(data) + 'eof').encode('utf-8'))