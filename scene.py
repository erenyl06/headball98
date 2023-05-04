from actors import Player1,Player2,Ground,Net,Ball
from config import Colors, Globals
import pygame
import os

class SceneManager(object):
    def __init__(self):
        self.go_to(GameScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

class Scene(object):
    def __init__(self):
        pass
    def render(self, screen):
        raise NotImplementedError
    def update(self):
        raise NotImplementedError
    def handle_events(self, events):
        raise NotImplementedError

player1Headpic = pygame.image.load(os.path.join('others','Head.png'))
pla1Head = pygame.transform.scale(player1Headpic,(70,70))

player2Headpic = pygame.image.load(os.path.join('others','Head2.png'))
pla2Head = pygame.transform.scale(player2Headpic,(70,70))

background = pygame.image.load(os.path.join('others','back.png'))
backgr = pygame.transform.scale(background,(Globals.win_width,Globals.win_height))

netpic = pygame.image.load(os.path.join('others','net.png'))
nettex = pygame.transform.scale(netpic,(20,175))

sandpic = pygame.image.load(os.path.join('others','sand.png'))
sandtex = pygame.transform.scale(sandpic,(Globals.win_width,105))

class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.player1 = Player1()
        self.player2 = Player2()
        self.ground = Ground()
        self.net = Net()
        self.points ={"player1": 0, "player2": 0}
        self.player1_score=self.font.render("{}".format(self.points["player1"]),1,Colors.white)
        self.player2_score=self.font.render("{}".format(self.points["player2"]),1, Colors.white)
        self.ball = Ball()

    def render(self,screen):
        screen.blit(backgr,(0,0))
        screen.blit(self.player1_score,(150,100))
        screen.blit(self.player2_score,(830,100))
        screen.blit(sandtex, (0,495))
        screen.blit(nettex, (Globals.win_width//2-10,320))
        screen.blit(pla1Head, (self.player1.x, self.player1.y))
        screen.blit(pla2Head, (self.player2.x, self.player2.y))
        pygame.draw.rect(screen,Colors.black,self.ball)


    def update(self):
        pressed = pygame.key.get_pressed()
        left,right,up = [pressed[key] for key in (pygame.K_LEFT, pygame.K_RIGHT,pygame.K_UP)]
        A, D, W = [pressed[key] for key in (pygame.K_a, pygame.K_d,pygame.K_w)]
        self.handle_point()
        self.player1.update(left,right,up)
        self.player2.update(A,D,W)
        self.ball.update(self.player1,self.player2)
        return

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pass

    def handle_point(self):

        def update_points(key) :
            self.points[key] +=1
            self.player1_score=self.font.render("{}".format(self.points["player1"]),1,Colors.black)
            self.player2_score=self.font.render("{}".format(self.points["player2"]),1,Colors.black)

        # if self.ball.x <= self.ball.width:
        #     update_points("player1")
        #     self.ball.reset()
        # if self.ball.x >= (Globals.win_width + self.ball.width):
        #     update_points("player2")
        #     self.ball.reset()
        #     self.ball.dir_x *= -1


