import pygame
import math
import random
class vecteur():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
class Fruit:
    def __init__(self):
        self.x =  random.randint(10,490)
        self.y = random.randint(10,490)
        self.taille = 10
    def Draw(self, ecran):
        pygame.draw.circle(ecran, (  255, 0, 0), (self.x,self.y), self.taille)

class Perso:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.taille = 10
        self.tab= None
        self.vit = 9
        self.score = 0
        self.dir ="none"
        self.position = [250, 250]
        self.body = []



    def Draw(self, ecran):
        pygame.draw.rect(ecran, (  0, 0, 255), pygame.Rect(self.x, self.y, 10, 10))
        for item in self.body:
            pygame.draw.rect(ecran, (  0, 0, 255), pygame.Rect(item.x, item.y, 10, 10))
        # pygame.draw.circle(ecran, (  0, 0, 255), (self.x,self.y), self.taille)

    def Update(self):
        if len(self.body)>0:
            temptab = []
            for a in self.body:
                temptab.append(vecteur(a.x,a.y))
            for i in range(len(self.body)):
                if i ==0:
                    self.body[0] = vecteur(self.x,self.y)
                else:
                    self.body[i] = vecteur(temptab[i-1].x,temptab[i-1].y)
        if self.dir == "up":
            self.y-=self.vit
        elif self.dir == "down":
            self.y+=self.vit
        elif self.dir == "left":
            self.x-=self.vit
        elif self.dir == "right":
            self.x+=self.vit

    def Collision(self, col):
        if col == None:
            return False
        xcol = col.x - self.x
        ycol = col.y - self.y
        distance = math.sqrt(xcol*xcol+ ycol*ycol)
        if distance < self.taille + col.taille :
            col.x = random.randint(10,490)
            col.y = random.randint(10,490)
            self.vit += 0.05
            self.score += 1
            self.body.append(vecteur(0,0))
            return True
        else:
            return False
