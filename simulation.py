import pygame
from screen import Screen
from entity import Entity

class Simulation:
    def __init__(self):
        self.scr = Screen(1500, 650)

    def infinite_loop(self):
        while 1 + 1 == 2:
            self.scr.screen.fill((100, 100, 100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break


    def create_entity(self, x, y, name, n):
        rocks = []
        papers = []
        scissors = []
        for i in range(n):
            entity = Entity(x, y, name)
            rocks.append(entity)
            print(len(rocks))


sim = Simulation()
sim.create_entity(12, 45, 77, 97)
sim.infinite_loop()
