import cv2
import torch
from gameState import GameState

model = torch.load('./myModel.pth')
model.eval()

env = GameState()
delayTime = 0

while env.alive:
    inputVals = [env.position[0], env.position[1], env.fruit_position[0], env.fruit_position[1], env.width, env.height]

    inputTensor = torch.FloatTensor(inputVals)
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

    env.update(newDirection)
    image = env.getImage()
    image = cv2.resize(image, (720, 720))

    cv2.imshow("Snake Window", image)
    cv2.waitKey(delayTime)