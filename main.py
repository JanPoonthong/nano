import pygame
import sys
import os


class Game:
    def __init__(self):
        self.size = self.width, self.height = 800, 800
        self.speed = [2, 2]
        self.black = 0, 0, 0
        self.dir = os.path.dirname(__file__)

    def run_game(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size, flags=pygame.DOUBLEBUF)
        ball = pygame.image.load(os.path.join(self.dir, "intro_ball.gif"))
        ballrect = ball.get_rect()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            ballrect = ballrect.move(self.speed)
            if ballrect.left < 0 or ballrect.right > self.width:
                self.speed[0] = -self.speed[0]
            if ballrect.top < 0 or ballrect.bottom > self.height:
                self.speed[1] = -self.speed[1]

            screen.fill(self.black)
            screen.blit(ball, ballrect)
            pygame.display.flip()


Game().run_game()
