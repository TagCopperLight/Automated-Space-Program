import pygame

from classes.client import Client


pygame.init()
pygame.font.init()

def main():
    client = Client((1280, 720), "Rocket Simulator", 60)

    client.run()

if __name__ == "__main__":
    main()