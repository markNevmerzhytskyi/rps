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
        self.scissors_texture = pygame.image.load('scissors.png')
        self.scissors_texture = pygame.transform.scale (self.scissors_texture, (30, 30))
        self.paper_texture = pygame.image.load('paper.png')
        self.paper_texture = pygame.transform.scale(self.paper_texture, (30, 30))
        self.rock_texture = pygame.image.load('rock.png')
        self.rock_texture = pygame.transform.scale(self.rock_texture, (30, 30))

    def infinite_loop(self):
        self.create_entity(300, 450, "rock", 27)
        self.create_entity(100, 200, "paper", 27)
        self.create_entity(500, 300, "scissors", 27)
        while 1 + 1 == 2:
            self.scr.screen.fill((100, 100, 100))
            for rock in self.rocks:
                minus = rock.x - 30, rock.y - 30
                plus = rock.x + 30, rock.y + 30
                rock.x += rock.direction[0]
                rock.y -= rock.direction[1]
                self.scr.screen.blit(self.rock_texture, (rock.x, rock.y))
                for paper in self.papers:
                    if paper.x < plus[0] and paper.x > minus[0] and paper.y < plus[1] and paper.y > minus[1]:
                        print("Paper wins")
                        self.who_wins(paper, rock)
                for scissors in self.scissors:
                    if scissors.x < plus[0] and scissors.x > minus[0] and scissors.y < plus[1] and scissors.y > minus[1]:
                        print("Rock wins")
                        self.who_wins(scissors, rock)
            for paper in self.papers:
                paper.x += paper.direction[0]
                paper.y -= paper.direction[1]
                self.scr.screen.blit(self.paper_texture, (paper.x, paper.y))
                for scissors in self.scissors:
                    minus = paper.x - 30, paper.y - 30
                    plus = paper.x + 30, paper.y + 30
                    if scissors.x < plus[0] and scissors.x > minus[0] and scissors.y < plus[1] and scissors.y > minus[1]:
                        print("Scissors wins!")
                        self.who_wins(scissors, paper)
            for scissors in self.scissors:
                scissors.x += scissors.direction[0]
                scissors.y -= scissors.direction[1]
                self.scr.screen.blit(self.scissors_texture, (scissors.x, scissors.y))
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

    def Move_barrier(self, entity):
        if entity.y >= 650:
            entity.y -= 10
        if entity.x >= 1500:
            entity.x -= 10
        if entity.y >= 0:
            entity.y += 10
        if entity.x >= 0:
            entity.x += 10

    def who_wins(self, entity1, entity2):
        if entity1 in self.rocks:
            if entity2 in self.scissors:
                self.scissors.remove(entity2)
            if entity2 in self.papers:
                self.rocks.remove(entity1)
        if entity1 in self.scissors:
            if entity2 in self.rocks:
                self.scissors.remove(entity1)
            if entity2 in self.papers:
                self.papers.remove(entity2)
        if entity1 in self.papers:
            if entity2 in self.rocks:
                self.rocks.remove(entity2)
            if entity2 in self.scissors:
                self.papers.remove(entity1)




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

