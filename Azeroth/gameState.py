import torch
import random

class GameState():
    def __init__(self):
        self.alive = True
        self.direction = 0
        self.body = [[10,5], [9,5], [8,5], [7,5]]
        self.position = self.body[0]
        self.width = 72
        self.height = 72 
        self.fruit_position = (random.randint(1, self.width), 
                    random.randint(1, self.height) )
        self.points = 0
        

    def update(self, newDirection):
        if not self.alive:
            return -100

        reward = -1
        self.direction = newDirection

        if self.direction == 0:
            self.position[1] += 1

        elif self.direction == 1:
            self.position[0] += 1

        elif self.direction == 2:
            self.position[1] -= 1

        elif self.direction == 3:
            self.position[0] -= 1

        if self.body[0] == self.fruit_position:
            self.points += 10
            reward = 10
            self.fruit_position = (random.randint(1, self.width), 
                    random.randint(1, self.height) )
            self.body.insert(0, self.position)

        else:
            for part in self.body:
                if self.direction == 0:
                    part[1] += 1

                elif self.direction == 1:
                    part[0] += 1

                elif self.direction == 2:
                    part[1] -= 1

                elif self.direction == 3:
                    part[0] -= 1

        if self.body[0][0] > self.width or self.body[0][0] < 0  or self.body[0][1] > self.height or self.body[0][1] < 0:
            self.alive = False
            return -100
        return reward 
            
        

        



        


        
