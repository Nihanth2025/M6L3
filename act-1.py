import pygame
import random
from pygame import mixer
mixer.init()
pygame.init()
surf_color="yellow"
color="blue"
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image=pygame.Surface([w,h])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,w,h))
        self.rect=self.image.get_rect()

    def moveRight(self,pix):
        self.rect.x +=pix
    def moveLeft(self,pix):
        self.rect.x -=pix
    def moveForward(self,speed):
        self.rect.y -=speed*speed/10
    def moveBackward(self,speed):
        self.rect.y +=speed*speed/10
    


pygame.init()
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Add Sprite")
all_sprite_list=pygame.sprite.Group()

sp1=Sprite(color,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,370)
all_sprite_list.add(sp1)

sp2=Sprite("orange",20,30)
sp2.rect.x=random.randint(0,480)
sp2.rect.y=random.randint(0,370)
all_sprite_list.add(sp2)

exit=True
clock=pygame.time.Clock()
while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False
    all_sprite_list.update()
    screen.fill(surf_color)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()