from typing import Any
import pygame 
import sys
pygame.init()
clock = pygame.time.Clock()

width, height = 1000, 700
window = pygame.display.set_mode((width,height))
window.fill((51, 0, 0))
aka = (255,69,0)
anim_count = 0
jump_count = 20
last_move = "right"

class Button_Menu():
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
       
    def draw(self, shift_x, shift_y):
        pygame.draw.rect(window, self.fill_color, self.rect, border_radius = 12)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
     
    def draw_image(self, images):
        self.images = pygame.image.load(images)
        window.blit(self.images, (self.rect.x, self.rect.y))
     
        
    def set_text(self, text, fsize=10, text_color=(255, 255, 255)):
        self.text = text
        self.image = pygame.font.SysFont('bmjapana12', fsize).render(text, True, text_color)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)  
    
class Player():
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
        
    def draw_image(self, images):
        self.images = pygame.image.load(images)
        window.blit(self.images, (self.rect.x, self.rect.y))
        
    def draw_ammo(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
        
    def move(self):
        if  not (self.rect.x <= -280):
            self.rect.x -= 5 
        else:
            window.fill((0, 255, 0))
            Finish = Button_Menu(150, 100, 410, 100, (0, 255, 0))
            Finish.set_text("Молодець, ти перепригнув ворога!", 30, (0, 0, 255))
            Finish.draw(0, 200)     

        
     
    
def fill():
    window.fill((3, 7, 44))
    window.blit(Zemlya, (0, 0))
    window.blit(Zemlya1, (300, 0))
    window.blit(Moon, (-100, -100))
    window.blit(Tree, (-80, 35))
    window.blit(Small_grass, (700, 69))
    
#кнопки     
Hello = Button_Menu(210, 0, 410, 80, (51, 0, 0))
Hello.set_text("Перепригни ворога", 30, aka)
Hello.draw(75, 30)

Button = Button_Menu(270, 100, 410, 100, (0, 0, 0))
Button.set_text("Грати", 30)
Button.draw(140, 40)

Button1 = Button_Menu(270, 400, 410, 100, (0, 0, 0))
Button1.set_text("Вийти", 30)
Button1.draw(140, 40)
spysok = [Button, Button1]
#ігрові елементи
Person = Player(100, 59, 30, 30, (0, 0, 0))
Enemy = Player(1000, 59, 30, 30, (0, 0, 0))

#гравець
AFK_anim = ['model/AFK/Person.png', 'model/AFK/AFK animation.png']
left_anim = ['model/left/left1.png', 'model/left/left2.png']
right_anim = ['model/right/right1.png', 'model/right/right2.png']
#ворог
enemy_anim = ['model/enemy 1.png', 'model/enemy 2.png']
#інші об'єкти
Zemlya = pygame.image.load('model/earth.png')
Zemlya1 = pygame.image.load('model/earth.png')
Tree = pygame.image.load('model/tree.png')
Moon = pygame.image.load('model/moon.png')
Small_grass = pygame.image.load('model/small grass.png')

afk = False
go_left = False
go_right = False
left = False
right = False
jump = False
      
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if spysok[0].collidepoint(x, y):
                fill()
                Click = Button_Menu(260, 200, 410, 100, (3, 7, 44))
                Click.set_text("Натисни любу клавішу, почати", 30)
                Click.draw(3, 43)
            elif spysok[1].collidepoint(x, y):
                pygame.quit()
                sys.exit()   
            
        if event.type == pygame.KEYUP:
            afk = True
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
         
        if event.type == pygame.KEYDOWN:
            go_left = True
            go_right = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_w:
                jump = True
     
                
    if not (Person.rect.colliderect(Enemy.rect)):
        if afk:
            last_move = "afk"
            fill()
            Enemy.draw_image(enemy_anim[anim_count])
            Person.draw_image(AFK_anim[anim_count])
            Enemy.move()
            if anim_count == 1:
                anim_count = 0
            else:
                anim_count += 1       
        if left:
            Person.rect.x -= 15  
            last_move = "left" 
            fill()
            Enemy.draw_image(enemy_anim[anim_count])
            Person.draw_image(left_anim[anim_count])
            Enemy.move()
        elif left:    
            if go_left:
                if anim_count == 1:
                    anim_count = 0
                else:
                    anim_count += 1
                    
        if right:
            Person.rect.x += 15
            last_move = "right"
            fill()
            Enemy.draw_image(enemy_anim[anim_count])
            Person.draw_image(right_anim[anim_count])
            Enemy.move()
        elif right:    
            if go_right:
                if anim_count == 1:
                    anim_count = 0
                else:
                    anim_count += 1 
        if jump:
            Person.rect.y -= jump_count
            jump_count -= 1
            if last_move == "afk":
                fill()
                Enemy.draw_image(enemy_anim[anim_count])
                Person.draw_image('model/AFK/jump.png')
                Enemy.move()
            elif last_move == "left":
                fill()
                Enemy.draw_image(enemy_anim[anim_count])
                Person.draw_image('model/left/jump left.png')
                Enemy.move()
            else:
                fill()
                Enemy.draw_image(enemy_anim[anim_count])
                Person.draw_image('model/right/jump right.png')
                Enemy.move()
            if jump_count < -20:
                fill()
                jump = False
                jump_count = 20  
    else:
        window.fill((0, 120, 215))
        game_over = Button_Menu(120, 270, 410, 100, (0, 120, 215))
        game_over.set_text(":( Вибач, але ти програв", 30)
        game_over.draw(140, 40)
                                                   
    pygame.display.update()
    clock.tick(60)