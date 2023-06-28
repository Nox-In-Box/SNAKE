import torch
from gameState import GameState
import models
#learning rate = lr - is a hyper parameter
lr = 1e-2

epochs = 10

model = models.Agent()

#optim = optimiser 
optim = torch.optim.Adam(model.parameters(), lr = lr)

for i in range (epochs):
    print(i)
    #env enviorment
    env = GameState()

    while env.alive:
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

        elif action ==1:
            newDirection = currentDirection
        
        elif newDirection == 2:
            newDirection = currentDirection + 1 
            if newDirection > 3:
                newDirection = 0
        else:
            print("you done wrong")

        env.update(newDirection)

        loss = -m.log_prob(action)*env.points
