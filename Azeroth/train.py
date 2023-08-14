import torch
from gameState import GameState
import models
import math
#learning rate = lr - is a hyper parameter
lr = 1e-1

epochs = 50

model = models.Agent()

#optim = optimiser 
optim = torch.optim.Adam(model.parameters(), lr = lr)

for i in range (epochs):
    print('epoch', i)
    #env enviorment
    env = GameState()

    turnNumber = 0
    rewardTotal = 0
    while env.alive and turnNumber <= 150:
        #if input vals is changed must also be changed in SnakeAITest
        inputVals = [env.position[0], env.position[1], env.fruit_position[0], env.fruit_position[1], env.width, env.height]

        inputTensor = torch.FloatTensor(inputVals)

        #probs = probobilties
        probs = model(inputTensor)
        m = torch.distributions.Categorical(probs)
        action = m.sample()
        currentDirection = env.direction
        if action == 0:
            newDirection = currentDirection - 1
            if newDirection < 0:
                newDirection = 3

        elif action == 1:
            newDirection = currentDirection
        
        elif action == 2:
            newDirection = currentDirection + 1 
            if newDirection > 3:
                newDirection = 0
        else:
            print("you done wrong")
    
        rewardTotal += env.update(newDirection)
        distToFruit = math.dist(env.position, env.fruit_position)
        loss = -m.log_prob(action)*distToFruit
        loss.backward()
        optim.step()
        turnNumber += 1
        #print(loss.item())


    print('total turns', turnNumber)
    print('game points', env.points)
torch.save(model, './myModel.pth')