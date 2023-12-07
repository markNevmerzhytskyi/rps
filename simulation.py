import pygame
from screen import Screen
from entity import Entity


class Simulation:
    def __init__(self):
        self.scr = Screen(1500, 650)
        self.rocks = []
        self.papers = []
        self.scissors = []
        self.create_entity(10, 23, "rocks", 27)

    def infinite_loop(self):
        while 1 + 1 == 2:
            self.scr.screen.fill((100, 100, 100))
            for i in self.rocks:
                pygame.draw.circle(self.scr.screen, (150, 45, 56), (i.x, i.y), 5)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

    def create_entity(self, x, y, name, n):
        for i in range(n):
            entity = Entity(x, y, name)
            self.rocks.append(entity)
            print(len(self.rocks))


sim = Simulation()
sim.infinite_loop()

