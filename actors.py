import pygame
from config import Globals, Colors
from math import cos,sin,radians,pi

class Player1(pygame.Rect):

    def __init__(self):
        super(Player1,self).__init__(20,425,70,70)
        self.velocity = 5
        self.gravity = 1
        self.jumpHeight = 15
        self.jumpVelocity = 0
        self.jump=False


    def update(self,left,right):

        if left and self.x >= 10:
            self.x -= self.velocity
        if right and self.x <= Globals.win_width/2 - (self.width +15):
            self.x += self.velocity



class Player2(pygame.Rect):
    def __init__(self):
        super(Player2,self).__init__(780,425,70,70)
        self.velocity = 5
        self.gravity = 1
        self.jumpHeight = 15
        self.jumpVelocity = 0
        self.jump = False

    def update(self, left, right):
        if left and self.x >= Globals.win_width/2 + 15:
            self.x -= self.velocity
        if right and self.x <= Globals.win_width - (self.width + 10):
            self.x += self.velocity

class Ground(pygame.Rect):
    def __init__(self):
        super(Ground,self).__init__(0,495,Globals.win_width,Globals.win_height)


class Net(pygame.Rect):
    def __init__(self):
        super(Net,self).__init__(Globals.win_width//2-10,320,20,175)


class Ball(pygame.Rect):
    def __init__(self):
        super(Ball,self).__init__(800,200,20,20)
        self.yVelocity = 0
        self.xVelocity = 10
        self.gravity=.3
        self.mass= 100
        self.bounce_stop = .3
        self.retention=.9
        self.angle = radians(270)
        self.dir_x = cos(self.angle)
        self.dir_y = -sin(self.angle)

    def check_gravity(self):
        if self.y < 475:
            self.yVelocity += self.gravity
        else:
            if self.yVelocity > self.bounce_stop:
                self.yVelocity = self.yVelocity * -1 * self.retention
            else:
                if abs(self.yVelocity) <= self.bounce_stop:
                    self.yVelocity = 0

        return self.yVelocity

    def reset(self,player1):
         self.x = 200
         self.y = 200
         self.angle = radians(270)
         self.dir_x = cos(self.angle)
         self.dir_y = -sin(self.angle)

    def update(self,player1,player2):
         self.y += self.yVelocity
         self.x += self.xVelocity
         self.handle_bound_collision()
         self.yVelocity = self.check_gravity()

         #self.handle_player_collision(player1,player2)


    def handle_bound_collision(self):
        if self.y <=  0:
            self.yVelocity = self.yVelocity * -1
        if self.x <=  0 or self.x>= Globals.win_width - 20:
            self.xVelocity = self.xVelocity * -1 * self.retention


    # def handle_player_collision(self,player1,player2):
    #
    #     intersectX = self.x
    #     if self.colliderect(player1):
    #         relativeIntersectx = (player1.x + (30)) - intersectX
    #         normalizedRelativeIntersectx = relativeIntersectx / (60 / 2)
    #         self.angle = radians(normalizedRelativeIntersectx * 60)
    #         self.dir_x = cos(self.angle)
    #         self.dir_y = -sin(self.angle)
    #
    #     if self.colliderect(player2):
    #         self.yVelocity = self.yVelocity * -1
    #
    #         print("anan")