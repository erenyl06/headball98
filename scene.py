from actors import Player1,Player2,Ground,Net,Ball
from config import Colors, Globals
import pygame

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
        screen.blit(self.player1_score,(150,100))
        screen.blit(self.player2_score,(830,100))
        pygame.draw.rect(screen, Colors.blue,self.ground)
        pygame.draw.rect(screen,Colors.yellow,self.net)
        pygame.draw.rect(screen,Colors.red,self.player1)
        pygame.draw.rect(screen,Colors.green,self.player2)
        pygame.draw.rect(screen,Colors.white,self.ball)

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
            self.player1_score=self.font.render("{}".format(self.points["player1"]),1,Colors.white)
            self.player2_score=self.font.render("{}".format(self.points["player2"]),1, Colors.white)

        # if self.ball.x <= self.ball.width:
        #     update_points("player1")
        #     self.ball.reset()
        # if self.ball.x >= (Globals.win_width + self.ball.width):
        #     update_points("player2")
        #     self.ball.reset()
        #     self.ball.dir_x *= -1


