import pygame
import sys

pygame.init()

display_width = 500
display_height = 500

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Timer')
clock = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont(None, 100)
currentTime = [0, 0, 0]
stop = True
while True:
    clock.tick(FPS)
    gameDisplay.fill(white)
    currentString = [f'0{i}' if len(str(i)) ==
                     1 else i for i in currentTime]
    img = font.render(
        f'{currentString[0]}:{currentString[1]}:{currentString[2]}', True, black)
    gameDisplay.blit(img, (107, 216))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            stop = not stop
    if not stop:
        currentTime[2] += 1
        for i in range(len(currentTime)):
            if currentTime[i] >= 60:
                if i == 0:
                    sys.exit('TimeError: Maximum Time has been reached.')
                else:
                    currentTime[i - 1] += 1
                    currentTime[i] = 0

    pygame.display.update()
