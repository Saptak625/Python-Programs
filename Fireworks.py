import pygame
import random
import sys
import math

pygame.init()

display_width = 1800
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Fireworks')
clock = pygame.time.Clock()
FPS = 60


class Particle():
    def __init__(self, position, velocity, acceleration, color, size, fade):
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
        self.color = color
        self.fade = fade
        self.faded = False
        self.fadecolor = 255
        self.size = size

    def updateParticle(self):
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def displayParticle(self):
        roundedPosition = [int(self.pos[0]), int(self.pos[1])]
        if self.fadecolor > 0:
            finalcolor = [0, 0, 0]
            if self.color == 4:
                for i in range(3):
                    finalcolor[i] = self.fadecolor
            else:
                finalcolor[self.color - 1] = self.fadecolor
            pygame.draw.circle(alphaSurface, finalcolor,
                               roundedPosition, int(self.size - 1))
        else:
            self.faded = True
        if self.fade:
            self.fadecolor -= 2

    def __repr__(self):
        return f'Particle:\n--->Position: {self.pos}\n--->Velocity: {self.vel}\n--->Acceleration: {self.acc}'


class Firework():
    def __init__(self):
        self.particles = []
        self.exploded = False
        self.finished = False
        self.mainParticle = Particle([random.randint(20, display_width - 20), display_height + random.randint(-10, 10)], [
                                     0, random.randint(-12, -10)], [0, 0.1], random.randint(0, 4), 7, False)

    def updateFirework(self):
        if not self.exploded:
            self.mainParticle.updateParticle()
        if self.particles != []:
            if not self.particles[0].faded:
                for i in range(len(self.particles)):
                    p = self.particles[i]
                    p.vel[0] *= 0.95
                    p.vel[1] *= 0.95
                    p.updateParticle()
            else:
                self.finished = True

    def displayFirework(self):
        if self.mainParticle.vel[1] < 0:
            # Display main particle
            self.mainParticle.displayParticle()
        else:
            self.exploded = True
            self.mainParticle.vel = [0, 0]
            self.mainParticle.acc = [0, 0]
            if self.particles == []:
                # Create random unit vectors
                numOfParticles = 100
                for i in range(numOfParticles):
                    randomScaler = random.randint(4, 7)
                    random_x = random.random()
                    random_x_Scaler = random.choice([1, -1])
                    random_y = math.sqrt(1 - (random_x)**2)
                    random_y_Scaler = random.choice([1, -1])
                    p = Particle(self.mainParticle.pos[:], [random_x * randomScaler * random_x_Scaler,
                                                            random_y * randomScaler * random_y_Scaler], [0, 0.01], self.mainParticle.color, 4, True)
                    self.particles.append(p)
            if not self.particles[0].faded:
                for i in range(len(self.particles)):
                    p = self.particles[i]
                    p.displayParticle()
            else:
                self.finished = True


fireworks = [Firework() for i in range(10)]
alphaSurface = pygame.Surface((display_width, display_height), pygame.SRCALPHA)
gameDisplay.fill(black)
while True:
    clock.tick(FPS)
    alphaSurface.fill(pygame.Color(0, 0, 0, 40))
    for i in range(len(fireworks)):
        firework = fireworks[i]
        firework.displayFirework()
        firework.updateFirework()
        if firework.finished:
            fireworks[i] = Firework()
    chance = random.random()
    if chance <= 0.01:
        fireworks.append(Firework())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    gameDisplay.blit(alphaSurface, (0, 0))
    pygame.display.update()