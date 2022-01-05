# name = input("entre ton prenom dans le terminal: ")
# print(f"bonjour {name} ca va")

# import pygame

# # verifier que tout les modules soit chargé
# module_charge = pygame.init()
# print(module_charge)

# # taille de l'ecran
# ecran = pygame.display.set_mode((500,500))
# pygame.display.set_caption("space invader 3000")


# loop = True
# i = 0
# while loop:
#     ecran.fill((0,0,0))
#     circle = pygame.draw.circle(ecran, ( 0, 0, 255), (i,250), 20)
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_j:
#                 i=i+1
#             if event.type == pygame.QUIT:
#                 loop = False

#     pygame.display.flip()

# pygame.quit()



from Player import *
import pygame 
import time

module_charge = pygame.init()
print(module_charge)

ecran = pygame.display.set_mode(( 500, 500))
pygame.display.set_caption("Projet Python PA")

loop = True
f = Fruit()
p = Perso()
score = 0   
color = (255 - 10*score, 193, 183)
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    ecran.blit(score_surface, score_rect)

def end():
    end_font = pygame.font.SysFont('Monserrat', 60)
    end_surface = end_font.render(
        'Votre score est : ' + str(score), True, (255, 0, 0))
    end_rect = end_surface.get_rect()
    end_rect.midtop = (500/2, 500/2)
    ecran.blit(end_surface, end_rect)
    pygame.display.flip()


clock = pygame.time.Clock()
trye = True
while trye:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                trye = False
            if event.key == pygame.K_l:
                loop = True
            if event.key == pygame.K_h:
                loop = True
                f = Fruit()
                p = Perso()
                score = 0   
        if event.type == pygame.QUIT:
            trye = False
    while loop:
        ecran.fill((color))
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p.dir = "up"
                if event.key == pygame.K_LEFT:
                    p.dir = "left" 
                if event.key == pygame.K_DOWN:
                    p.dir = "down"
                if event.key == pygame.K_RIGHT:
                    p.dir = "right"
                if event.key == pygame.K_p:
                    loop = False     
                    ecran.blit(pygame.font.SysFont('Monserrat', 25).render('Appuyez sur P pour quittez', True, (255, 0, 0)),(0, 480))            
                    ecran.blit(pygame.font.SysFont('Monserrat', 20).render('Appuyez sur L pour revenir au jeu ', True, (255, 0, 0)),(280, 0))
                    ecran.blit(pygame.font.SysFont('Monserrat', 20).render('Appuyez sur H pour recomencer ', True, (255, 0, 0)),(280, 480))
            if event.type == pygame.QUIT:
                loop = False
        if  p.x < 0 or p.x > 500 or p.y < 0 or p.y > 500:
                end()
                loop = False
        if p.Collision(f):
            score += 1
        p.Update()
        p.Draw(ecran)
        ecran.blit(pygame.font.SysFont('Monserrat', 25).render('Appuyez sur P pour aller au menu', True, (255, 0, 0)),(0, 480))            
        show_score(0, (255, 255, 255), 'Monserrat', 25)
        if f:
            f.Draw(ecran)
        pygame.display.flip()
pygame.quit()
