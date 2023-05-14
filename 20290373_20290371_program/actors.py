import pygame
from config import Globals, Colors
from math import cos,sin,radians,pi

class Player1(pygame.Rect):

    def __init__(self):
        super(Player1,self).__init__(20,415,80,80)
        self.velocity = 10
        self.gravity = 1


    def update(self,left,right):

        if left and self.x >= 10:
            self.x -= self.velocity
        if right and self.x <= Globals.win_width/2 - (self.width +15):
            self.x += self.velocity



class Player2(pygame.Rect):
    def __init__(self):
        super(Player2,self).__init__(780,415,80,80)
        self.velocity = 10
        self.gravity = 1

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
        super(Ball,self).__init__(800,100,20,20)
        self.yVelocity = 0
        self.xVelocity = 0
        self.gravity=.1
        self.bounce_stop = .3
        self.retention=.9


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

    def reset1(self):
        self.x = 200
        self.y = 100
        self.xVelocity =0
        self.yVelocity =0
    def reset2(self):
        self.x = 800
        self.y = 100
        self.xVelocity = 0
        self.yVelocity = 0


    def update(self,player1,player2):
         self.y += self.yVelocity
         self.x += self.xVelocity

         self.yVelocity = self.check_gravity()
         self.handle_bound_collision()
         self.handle_player_collision(player1,player2)


    def handle_bound_collision(self):
        if self.y <= 0:
            self.yVelocity = self.yVelocity * -1

        if self.x <=  0 or self.x >= Globals.win_width - 20 :
            self.xVelocity = self.xVelocity * -1 * self.retention

        if self.y <=  Globals.win_height and self.y >= 300:
            if self.x <=  Globals.win_width/2+10 and (self.x >= Globals.win_width / 2 - 30):
                self.xVelocity = self.xVelocity * -1 * self.retention

        if self.yVelocity>0:
            if self.x <= Globals.win_width/2 + 10 and self.x >= Globals.win_width/2 - 30:
                if self.y >= 300:
                    self.yVelocity = self.yVelocity * -1 * self.retention





    def handle_player_collision(self,player1,player2):

        if self.colliderect(player1):
            if self.yVelocity > 0:
                if self.x >= player1.x and self.x <= player1.x + 80:
                    if self.y  >= player1.y:
                        self.yVelocity *= -1.01

                        middle_x = player1.x + 40
                        difference_x = middle_x - (self.x+10)
                        reduction = 40 / self.yVelocity
                        self.xVelocity = difference_x / reduction * 0.9


        if self.colliderect(player2):
            if self.yVelocity > 0:
                if self.x >= player2.x and self.x <= player2.x + 80:
                    if self.y >= player2.y:
                        self.yVelocity *= -1.02

                        middle_x = player2.x + 40
                        difference_x = middle_x - (self.x+10)
                        reduction = 40 / self.yVelocity
                        self.xVelocity = difference_x / reduction * 0.9
