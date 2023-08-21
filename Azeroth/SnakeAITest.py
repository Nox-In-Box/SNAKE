import pygame
import time 
import random 
import torch

model = torch.load('./myModel.pth')
model.eval()
snake_speed = 1

window_x = 720 
window_y = 720

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

pygame.init()

pygame.display.set_caption('NOX_SNAKE')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100,50]
snake_body = [[100,50], [90,50], [80,50], [70,50]]

fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                    random.randrange(1, (window_y//10)) * 10]


fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0 

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score : ' + str(score), True,color)

    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)


def game_over():

    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render('Your score is:' + str(score), True, red)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/4)

    game_window.bilt(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

    quit()

currentDirection = 1
while True:
    #goes in input vals ----> x of snake head, y of snake head, x of fruit_position, y of fruit_position, height, width
    inputVals = [snake_position[0], snake_position[1], fruit_position[0], fruit_position[1], window_y, window_x]

    inputTensor = torch.FloatTensor(inputVals)

    probs = model(inputTensor)
    m = torch.distributions.Categorical(probs)
    action = (int(m.sample().item()))
    print(action)
    if action == 0:
        print("going left")
        newDirection = currentDirection -1
        print(newDirection)
        if newDirection == 0 and newDirection - 1 <= 0:
            newDirection = 3

    elif action ==1:
        newDirection = currentDirection
    
    elif action == 2:
        newDirection = currentDirection + 1 
        if newDirection > 3:
            newDirection = 0
    else:
        print("you done wrong")

    if newDirection == 0:
        change_to = 'UP'
    elif newDirection == 1:
        change_to = 'RIGHT'
    elif newDirection== 2:
        change_to = 'DOWN'
    elif newDirection == 3:
        change_to = 'LEFT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction!= 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10
    
    print(change_to)

    snake_body.insert(0, list(snake_position))
    if (snake_position[0]-5 <= fruit_position[0] <= snake_position[0]+5) and (snake_position[1]-5 <= fruit_position[1] <= snake_position[1]+5):
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
        random.randrange(1, (window_y//10) * 10)]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame. Rect(
            pos[0], pos[1], 10, 10)
        )

    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10)
    )

    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(snake_speed)




    

