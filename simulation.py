import pygame
from screen import Screen
from entity import Entity
import random


class Simulation:
    def __init__(self):
        self.scr = Screen(1500, 650)
        self.rocks = []
        self.papers = []
        self.scissors = []
        self.rocks_color = (67, 45, 45)
        self.papers_color = (150, 86, 56)
        self.scissors_color = (56, 99, 52)

    def infinite_loop(self):
        self.create_entity(300, 450, "rock", 27)
        self.create_entity(100, 200, "paper", 27)
        self.create_entity(500, 300, "scissors", 27)
        while 1 + 1 == 2:
            self.scr.screen.fill((100, 100, 100))
            for rock in self.rocks:
                rock.x += rock.direction[0]
                rock.y -= rock.direction[1]
                pygame.draw.circle(self.scr.screen, self.rocks_color, (rock.x, rock.y), 5)
            for paper in self.papers:
                paper.x += paper.direction[0]
                paper.y -= paper.direction[1]
                pygame.draw.circle(self.scr.screen, self.papers_color, (paper.x, paper.y), 5)
            for scissors in self.scissors:
                scissors.x += scissors.direction[0]
                scissors.y -= scissors.direction[1]
                pygame.draw.circle(self.scr.screen, self.scissors_color, (scissors.x, scissors.y), 5)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

    def create_entity(self, x, y, name, n):
        for i in range(n):
            entity = Entity(x + random.randint(0, 200), y + random.randint(0, 150), name)
            if name == "rock":
                self.rocks.append(entity)
            if name == "paper":
                self.papers.append(entity)
            if name == "scissors":
                self.scissors.append(entity)


sim = Simulation()
sim.infinite_loop()

