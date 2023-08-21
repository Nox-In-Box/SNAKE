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
        #if you aren't alive you get -100 reward
        if not self.alive:
            return -100
        #everytime you do good you get -.01 reward (i'm not sure why we did this, why  isn't this positive?)
        reward = .01
        #declaring newDirection
        self.direction = newDirection
        #if direction = 0 (which is up) then you add one to the y coordinate
        if self.direction == 0:
            self.position[1] += 1
        #if direction = 1(right) then you add one to the x coordinate 
        elif self.direction == 1:
            self.position[0] += 1
        # if direction = 2(down) then you subtract one from the y coordinate
        elif self.direction == 2:
            self.position[1] -= 1
        #if direction = 3(left) then you subtract on from the x coordinate
        elif self.direction == 3:
            self.position[0] -= 1
    
        #if the head of the body (first x and y coordinate of the body) matches the coordinates of the fruit
        #and you get 10 points in game and a reward of 10 
        if self.body[0] == self.fruit_position:
            self.points += 10
            reward = 10
            #resets the fruit to be in a random place
            self.fruit_position = (random.randint(1, self.width), 
                    random.randint(1, self.height) )
            self.body.insert(0, self.position)
        else:
            copyBody = self.body.copy()
            
            self.body[0] = self.position
            
            for i in range(1,(len(copyBody))):
                self.body[i] = copyBody[i-1]
            
            #SIMPLE BUT NOT BEST ALGORITHM
            #copy the current body
            #set the current bodies head to self.position
            #for i in (1 to length of body), set self.body[i] = copyBody[i-1]

        if self.body[0][0] > self.width or self.body[0][0] < 0  or self.body[0][1] > self.height or self.body[0][1] < 0:
            self.alive = False
            return -100
        return reward 
    
