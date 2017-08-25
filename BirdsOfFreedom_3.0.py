
#Projeto Integrador - 2 Semestre - Tecnologia em Jogos Digitais
#Jogo: Birds of Freedom
#Genero: Runner
#Grupo: Patience & Time
#Integrantes: Eduardo Salvatore, Martim Rubino

#--------------------------------------------------------------------------------------------------------------------------

#Importando os modulos necessarios
import pygame
import random
import os
from os import path
import pickle

#-------------------------------------------------------------------------------------------------------------------------- 
#Definindo meu fps e o tamanho da minha tela
FPS = 30
WIDTH = 1224
HEIGHT = 840

#Definindo cores que usarei
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


#-------------------------------------------------------------------------------------------------------------------------- 
#Iniciando o pygame
pygame.init()

#Imprtando um arquivo highscore
try:
    with open('highscoreA.dat', 'rb') as file:
        highA = pickle.load(file)
except:
    highA = 0
#Imprtando um arquivo highscore
try:
    with open('highscoreB.dat', 'rb') as file:
        highB = pickle.load(file)
except:
    highB = 0
#Imprtando um arquivo highscore
try:
    with open('highscoreC.dat', 'rb') as file:
        highC = pickle.load(file)
except:
    highC = 0
#Imprtando um arquivo highscore
try:
    with open('highscoreD.dat', 'rb') as file:
        highD = pickle.load(file)
except:
    highD = 0


#Declarando o tamanho da tela e sua legenda
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BIRDS OF FREEDOM")

clock = pygame.time.Clock()

#Setando as pastas dos meus assets
game_folder = os.path.dirname("__file__")
img_folder = os.path.join(game_folder, "img")


#--------------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------

        #SEC-A                #DEFINICAO DE CLASSES

#--------------------------------------------------------------------------------------------------------------------------




#Definindo a classe para meu jogador
class Player(pygame.sprite.Sprite):
    #Sprite do meu jogador
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Player.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 1150
        self.rect.bottom = HEIGHT / 2
        self.posx =  WIDTH - 1150
        self.posy =  HEIGHT / 2
        self.velx = 0
        self.vely = 0
        self.acx = 0
        self.acy = 0
        self.gravidade = 0.8

    
    def jump(self):
        self.vely = -12
        
        
        
    def update(self):
        self.acx = 0
        self.acy = self.gravidade
        
        keystate = pygame.key.get_pressed()
        
       
        #Calculando o deslocamento para a esquerda do meu jogador
        if keystate[pygame.K_LEFT]:
            self.acx = -0.5
        #Calculando o deslocamento para a direita do meu jogador
        if keystate[pygame.K_RIGHT]:
             self.acx = 0.5

        #Calculando a veloidade de deslocamento e a posicao do meu jogador
        self.velx += self.acx
        self.posx += self.velx + 0.5 * self.acx

        #Calculando a gravidade e velocidade de queda do meu jogador
        self.vely += self.acy
        self.posy += self.vely + 0.5 * self.acy

        #Atualizando a posicao x do meu jogador
        self.rect.centerx = self.posx

        #Atualizando a posicao y do meu jogador
        self.rect.centery = self.posy


#--------------------------------------------------------------------------------------------------------------------------
#Definindo uma classe para meus inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "enemy.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.centery = random.randrange(0, 790)
        self.rect.centerx = random.randrange(1224, 1324)
        self.velx = random.randrange(-15,-7)

    def update(self):
        self.rect.x += self.velx
        if self.rect.centerx < 5:
            self.rect.centerx = random.randrange(1224, 1324)
            self.rect.centery = random.randrange(0, 790)


#--------------------------------------------------------------------------------------------------------------------------

#Definindo uma classe para meu inimigo especial
class Inimigo2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "enemy2.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(5000, 10000)
        self.rect.centery = random.randrange(0, 790)
        self.velx = -15
        self.vely = 15

    def update(self):
        self.rect.x += self.velx*1.5
        self.rect.y += self.vely
        if self.rect.centerx < 0:
            self.rect.centerx = random.randrange(5000, 10000)
            self.rect.centery = random.randrange(0, 790)
        if self.rect.centery > 790:
            self.vely = -25
        if self.rect.centery < 50:
            self.vely = 25
            


#--------------------------------------------------------------------------------------------------------------------------


#Definindo uma classe para meus itens de ponto
class Item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "item.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.centery = random.randrange(0, 790)
        self.rect.centerx = random.randrange(1224, 1324)
        self.velx = random.randrange(-15,-2)

    def update(self):
        self.rect.x += self.velx
        if self.rect.centerx < 5:
            self.rect.centerx = random.randrange(1224, 1324)
            self.rect.centery = random.randrange(0, 790)

#--------------------------------------------------------------------------------------------------------------------------
#Definindo uma classe para meu ponto especial
class Special(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "special.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.centery = random.randrange(0, 790)
        self.rect.centerx = random.randrange(1224, 1324)
        self.velx = random.randrange(-15,-10)

    def update(self):
        self.rect.x += self.velx
        if self.rect.centerx < 5:
            self.rect.centerx = random.randrange(1224, 1324)
            self.rect.centery = random.randrange(0, 790)
            
         
#-------------------------------------------------------------------------------------------------------------------------- 
#Criando uma classe para minhas plataformas (Servem apenas para limitacao do cenario)
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



#--------------------------------------------------------------------------------------------------------------------------

         #SEC-B                  #DEFINICAO DE FUNCOES

#--------------------------------------------------------------------------------------------------------------------------


        

#Funcao que calcula a pontuacao do jogador
def Score(pontos, high):
    fonte = pygame.font.SysFont(None, 80)
    text = fonte.render("SCORE: "+str(pontos), True, WHITE)
    textB = fonte.render("BEST: "+str(high), True, WHITE)
    screen.blit(text,(530,780))
    screen.blit(textB,(950,780))

    if score > high:
        text = fonte.render("SCORE: "+str(pontos), True, YELLOW)
        screen.blit(text,(530,780))
        
#--------------------------------------------------------------------------------------------------------------------------

#Funcao que mostra a vida do jogador
def Vida(hp):
    if hp < 10:
        fonte = pygame.font.SysFont(None, 80)
        text = fonte.render("ENERGY: "+str(hp)+"%", True, RED)
        screen.blit(text,(50,780))
    else:
        fonte = pygame.font.SysFont(None, 80)
        text = fonte.render("ENERGY: "+str(hp)+"%", True, WHITE)
        screen.blit(text,(50,780))

#--------------------------------------------------------------------------------------------------------------------------

#Funcao que define minha tela de game over
def telaGameover(high_score):
    if high_score:
        screen.blit(gameoverImageB, [0, 0])
        fonte = pygame.font.SysFont(None, 200)
        text = fonte.render(""+str(score), True, BLACK)
        screen.blit(text,(580,500))
        pygame.display.flip()
        espera = True
        while espera:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameloop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        espera = False
    else:
        screen.blit(gameoverImage, [0, 0])
        fonte = pygame.font.SysFont(None, 200)
        text = fonte.render(""+str(score), True, BLACK)
        screen.blit(text,(800,435))
        pygame.display.flip()
        espera = True
        while espera:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameloop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        espera = False
    


#--------------------------------------------------------------------------------------------------------------------------

#Definindo a funcao que ira tocar as musicas do meu jogo
def playMusic(gamestate):
    #Toca a musica dos menus
    if gamestate == 1:
        pygame.mixer.music.load("menutheme.ogg")
        pygame.mixer.music.play(-1)
    #Toca a musica do jogo rodando
    if gamestate == 2:
        pygame.mixer.music.load("playtheme.ogg")
        pygame.mixer.music.play(-1)
    if gamestate == 3:
        pygame.mixer.music.load("udedtheme.ogg")
        pygame.mixer.music.play(-1)



#--------------------------------------------------------------------------------------------------------------------------

         #SEC-C                #INSTANCIANDO E CHAMANDO MINHAS CLASSES E OBJETOS

#--------------------------------------------------------------------------------------------------------------------------

        
        
#Criando um grupo para meus sprites
all_sprites = pygame.sprite.Group()
all_spritesB = pygame.sprite.Group()
#Criando um grupo para meus inimigos
inimigos = pygame.sprite.Group()
#Criando um grupo para meu inimigo especial
inimigo2 = pygame.sprite.Group()
#Criando um grupo para minhas plataformas
platforms = pygame.sprite.Group()
#Criando um grupo para meus itens de pontuacao
items = pygame.sprite.Group()
#Criando um grupo para meu item especial
special = pygame.sprite.Group()

#-------------------------------------------------------------------------------------------------------------------------- 
#Insanciando um objeto player
player = Player()
#Adicionando meu objeto player ao meu grupo de sprites
all_sprites.add(player)

#--------------------------------------------------------------------------------------------------------------------------

#Instanciando o objeto do meu inimigo especial (So aparece na dificuldade maxima)
m2 = Inimigo2()
all_spritesB.add(m2)
inimigo2.add(m2)

#--------------------------------------------------------------------------------------------------------------------------
#Usando um laco para criar um inimigo
for i in range(6):
    m = Inimigo()
    #Adicionando meu objeto inimigo ao grupo de sprites
    all_sprites.add(m)
    #Adicionando meu objeto inimigo ao grupo de inimigos 
    inimigos.add(m)

#--------------------------------------------------------------------------------------------------------------------------

#Usando um laco para criar meus itens de ponto
for i in range(3):
    p = Item()
    #Adicionando meu objeto ponto ao grupo de sprites
    all_sprites.add(p)
    #Adicionando meu objeto ponto ao grupo de itens
    items.add(p)

#--------------------------------------------------------------------------------------------------------------------------

#Usando um laco para criar meus itens de ponto
for i in range(1):
    s = Special()
    #Adicionando meu objeto ponto ao grupo de sprites
    all_sprites.add(s)
    #Adicionando meu objeto ponto ao grupo de itens
    special.add(s)

#--------------------------------------------------------------------------------------------------------------------------
    
#Instanciando um objeto plataforma
#             x      y        w     h
p1 = Platform(0, HEIGHT-50, WIDTH, 50)
p2 = Platform(-10, 0, 10, HEIGHT)
p3 = Platform(0, -10, WIDTH, 10)
p4 = Platform(WIDTH, 0, 10, HEIGHT)

#Adicionando meu objeto plataforma ao meu grupo de sprites
all_sprites.add(p1)
all_sprites.add(p2)
all_sprites.add(p3)
all_sprites.add(p4)

#Adicionando meu objeto plataforma ao meu grupo de plataformas
platforms.add(p1)
platforms.add(p2)
platforms.add(p3)
platforms.add(p4)


#-------------------------------------------------------------------------------------------------------------------------- 
#Importando as imagens dos menus
menuprincipal_image = pygame.image.load("MenuPrincipal.png").convert()
menuhelp_image = pygame.image.load("MenuHelp.png").convert()
menucreditos_image = pygame.image.load("MenuCreditos.png").convert()



#--------------------------------------------------------------------------------------------------------------------------     
        
          #SEC-D                   #GAME LOOP
          
#--------------------------------------------------------------------------------------------------------------------------



#Definindo meu gameloop

#carregando as imagens do meu parallax
bottomImage = pygame.image.load("bottom.png").convert()
midbottomImage = pygame.image.load("midbottom.png").convert()
midtopImage = pygame.image.load("midtop.png").convert()
topImage = pygame.image.load("top.png").convert()

#Carregando as imagens de game over
gameoverImage = pygame.image.load("gameover.png").convert()
gameoverImageB = pygame.image.load("gameoverB.png").convert()

#Carregando o fundo para minha dificuldade maxima
bottomded = pygame.image.load("bottomded.png").convert()

#Carregando a imagem com o logo do gurpo
image = pygame.image.load("grouplogo.png").convert()

#Gerando minha chuva
rain_list = []
for i in range(1000):
    x = random.randrange(0, 1224)
    y = random.randrange(0, 840)
    rain_list.append([x, y])

#Lista para detalhes do cenario
detalhe_list = []
for i in range(100):
    x = random.randrange(0, 1224)
    y = 0
    detalhe_list.append([x, y])


#definindo as variaveis de velocidade do meu parallax
mbX = 0
mtX = 0
tX = 0

uded = False

dif = 0

valor = 0
hp = 0
i=1
logo = True
high_score = False
score = 0
menu = 0
gamestate = 1
game_over = False
gameloop = True
while gameloop:
    clock.tick(FPS)
    playMusic(gamestate)

    while logo:
        i += 0.5
        screen.fill((0,0,0))
        image.set_alpha(i)
        logoimage = screen.blit(image,(0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = 255

        if i == 255:
            logo = False
            menu = 1
    #-------------------------------------------------------------------------------------------------------------------------- 
    #Menu principal do meu jogo
    while menu == 1:
        screen.blit(menuprincipal_image, [0, 0])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound('select.ogg').play()
                    menu = 4
                if event.key == pygame.K_a:
                    pygame.mixer.Sound('select.ogg').play()
                    menu = 2
                    break
                if event.key == pygame.K_z:
                    pygame.mixer.Sound('select.ogg').play()
                    menu = 3
                    break
            #Flip do display
            pygame.display.flip()  

    #--------------------------------------------------------------------------------------------------------------------------     
    #Menu de controles do meu jogo
    while menu == 2:
        
        screen.blit(menuhelp_image, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pygame.mixer.Sound('select.ogg').play()
                    menu = 1
                    break
        #Flip do display
        pygame.display.flip()
        
    #--------------------------------------------------------------------------------------------------------------------------    
    #Menu de creditos do meu jogo
    while menu == 3:
        
        screen.blit(menucreditos_image, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    pygame.mixer.Sound('select.ogg').play()
                    menu = 1
                    break
        #Flip do display
        pygame.display.flip()
        
    #--------------------------------------------------------------------------------------------------------------------------

    #Tela de dificuldades
    while menu == 4:
        fonte = pygame.font.SysFont(None, 100)
        textA = fonte.render("A - EASY", True, WHITE)
        textB = fonte.render("S - MEDIUM", True, WHITE)
        textC = fonte.render("D - HARD", True, WHITE)
        textD = fonte.render("F - INSANITY", True, RED)
        screen.fill(BLACK)
        screen.blit(textA,(450,100))
        screen.blit(textB,(450,300))
        screen.blit(textC,(450,500))
        screen.blit(textD,(450,700))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pygame.mixer.Sound('start.ogg').play()
                    dif = 1
                    valor = 30
                    hp = valor
                    menu = 5
                    gamestate = 2
                    playMusic(gamestate)
                    break
                if event.key == pygame.K_s:
                    pygame.mixer.Sound('start.ogg').play()
                    dif = 2
                    valor = 20
                    hp = valor
                    menu = 5
                    gamestate = 2
                    playMusic(gamestate)
                    break
                if event.key == pygame.K_d:
                    pygame.mixer.Sound('start.ogg').play()
                    dif = 3
                    valor = 10
                    hp = valor
                    menu = 5
                    gamestate = 2
                    playMusic(gamestate)
                    break
                if event.key == pygame.K_f:
                    pygame.mixer.Sound('start.ogg').play()
                    dif = 4
                    valor = 2
                    hp = valor
                    uded = True
                    menu = 5
                    gamestate = 3
                    playMusic(gamestate)
                    break
                    

    #--------------------------------------------------------------------------------------------------------------------------

        
    #Execucao do meu jogo principal (Jogo rodando)
    while menu == 5:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = 1
                    gamestate = 1
                    break
                if event.key == pygame.K_UP:
                    player.jump()

        #Verificando a vida do jogador, caso esteja em 0 o programa roda o game over
        if hp < 0:
            game_over = True
        
        #Definindo o meu game over
        if game_over and dif == 1:
            
            if score > highA:
                high_score = True
                with open('highscoreA.dat', 'wb') as file:
                    pickle.dump(score, file)
                telaGameover(high_score)
                playMusic(gamestate)
                game_over = False
                hp = valor
                score = 0
                mbX = 0
                mtX = 0
                tX = 0

                #Relendo o arquivo de highscore
                try:
                    with open('highscoreA.dat', 'rb') as file:
                        highA = pickle.load(file)
                except:
                    highA = 0
                
                player = Player()    
                all_sprites.add(player)
                for inimigo in inimigos:
                    inimigo.rect.x = random.randrange(1224, 1324)
                    inimigo.rect.y = random.randrange(0, 800)
                for inimigo in inimigo2:
                    inimigo.rect.x = random.randrange(5000, 10000)
                    inimigo.rect.y = 0
            else:
                high_score = False
                telaGameover(high_score)
                playMusic(gamestate)
                game_over = False
                hp = valor
                score = 0
                mbX = 0
                mtX = 0
                tX = 0

                #Relendo o arquivo de highscore
                try:
                    with open('highscoreA.dat', 'rb') as file:
                        highA = pickle.load(file)
                except:
                    highA = 0
                
                player = Player()    
                all_sprites.add(player)
                for inimigo in inimigos:
                    inimigo.rect.x = random.randrange(1224, 1324)
                    inimigo.rect.y = random.randrange(0, 800)
                for inimigo in inimigo2:
                    inimigo.rect.x = random.randrange(5000, 10000)
                    inimigo.rect.y = 0

            #Definindo o meu game over
        if game_over and dif == 2:
            
            if score > highB:
                high_score = True
                with open('highscoreB.dat', 'wb') as file:
                    pickle.dump(score, file)
                telaGameover(high_score)
                playMusic(gamestate)
                game_over = False
                hp = valor
                score = 0
                mbX = 0
                mtX = 0
                tX = 0

                #Relendo o arquivo de highscore
                try:
                    with open('highscoreB.dat', 'rb') as file:
                        highB = pickle.load(file)
                except:
                    highB = 0
                
                player = Player()    
                all_sprites.add(player)
                for inimigo in inimigos:
                    inimigo.rect.x = random.randrange(1224, 1324)
                    inimigo.rect.y = random.randrange(0, 800)
                for inimigo in inimigo2:
                    inimigo.rect.x = random.randrange(5000, 10000)
                    inimigo.rect.y = 0
            else:
                high_score = False
                telaGameover(high_score)
                playMusic(gamestate)
                game_over = False
                hp = valor
                score = 0
                mbX = 0
                mtX = 0
                tX = 0

                #Relendo o arquivo de highscore
                try:
                    with open('highscoreB.dat', 'rb') as file:
                        highB = pickle.load(file)
                except:
                    highB = 0
                
                player = Player()    
                all_sprites.add(player)
                for inimigo in inimigos:
                    inimigo.rect.x = random.randrange(1224, 1324)
                    inimigo.rect.y = random.randrange(0, 800)
                for inimigo in inimigo2:
                    inimigo.rect.x = random.randrange(5000, 10000)
                    inimigo.rect.y = 0

            #Definindo o meu game over
        if game_over and dif == 3:
            
            if score > highC:
                high_score = True
                with open('highscoreC.dat', 'wb') as file:
                    pickle.dump(score, file)
                telaGameover(high_score)
                playMusic(gamestate)
                game_over = False
                hp = valor
                score = 0
                mbX = 0
                mtX = 0
                tX = 0

                #Relendo o arquivo de highscore
                try:
                    with open('highscoreC.dat', 'rb') as file:
                        highC = pickle.load(file)
                except:
                    highC = 0
                
                player = Player()    
                all_sprites.add(player)
                for inimigo in inimigos:
                    inimigo.rect.x = random.randrange(1224, 1324)
                    inimigo.rect.y = random.randrange(0, 800)
                for inimigo in inimigo2:
                    inimigo.rect.x = random.randrange(5000, 10000)
                    inimigo.rect.y = 0
            else:
                high_score = False
                telaGameover(high_score)
                playMusic(gamestate)
                game_over = False
                hp = valor
                score = 0
                mbX = 0
                mtX = 0
                tX = 0

                #Relendo o arquivo de highscore
                try:
                    with open('highscoreC.dat', 'rb') as file:
                        highC = pickle.load(file)
                except:
                    highC = 0
                
                player = Player()    
                all_sprites.add(player)
                for inimigo in inimigos:
                    inimigo.rect.x = random.randrange(1224, 1324)
                    inimigo.rect.y = random.randrange(0, 800)
                for inimigo in inimigo2:
                    inimigo.rect.x = random.randrange(5000, 10000)
                    inimigo.rect.y = 0
            #Definindo o meu game over
        if game_over and dif == 4:
            
            if score > highD:
                high_score = True
                with open('highscoreD.dat', 'wb') as file:
                    pickle.dump(score, file)
                telaGameover(high_score)
                playMusic(gamestate)
                game_over = False
                hp = valor
                score = 0
                mbX = 0
                mtX = 0
                tX = 0

                #Relendo o arquivo de highscore
                try:
                    with open('highscoreD.dat', 'rb') as file:
                        highD = pickle.load(file)
                except:
                    highD = 0
                
                player = Player()    
                all_sprites.add(player)
                for inimigo in inimigos:
                    inimigo.rect.x = random.randrange(1224, 1324)
                    inimigo.rect.y = random.randrange(0, 800)
                for inimigo in inimigo2:
                    inimigo.rect.x = random.randrange(5000, 10000)
                    inimigo.rect.y = 0
            else:
                high_score = False
                telaGameover(high_score)
                playMusic(gamestate)
                game_over = False
                hp = valor
                score = 0
                mbX = 0
                mtX = 0
                tX = 0

                try:
                    with open('highscoreD.dat', 'rb') as file:
                        highD = pickle.load(file)
                except:
                    highD = 0
                
                player = Player()    
                all_sprites.add(player)
                for inimigo in inimigos:
                    inimigo.rect.x = random.randrange(1224, 1324)
                    inimigo.rect.y = random.randrange(0, 800)
                for inimigo in inimigo2:
                    inimigo.rect.x = random.randrange(5000, 10000)
                    inimigo.rect.y = 0

            
            

        #Update
        if uded == True:
            all_sprites.update()
            all_spritesB.update()
        else:
            all_sprites.update()

        #Fazendo o update da minha parallax
        if mbX <= -1224:
            mbX = 0
        if mtX <= -1224:
            mtX = 0
        if tX <= -1224:
            tX = 0
        mbX -= 1
        mtX -= 3
        tX -= 5

        #Colisao com as plataformas do jogo, linimitacao da area jogavel
        col = pygame.sprite.spritecollide(player, platforms, False)
        if col:
            for i in range(len(col)):
            
                if col[i] == p1:
                    player.posy = col[i].rect.top - player.rect.height / 2
                    player.vely = 0
                elif col[i] == p2:
                    player.posx = col[i].rect.right + 43    
                    player.velx = 0
                elif col[i] == p3:
                    player.posy = col[i].rect.bottom + player.rect.height / 2
                elif col[i] == p4:
                    player.posx = col[i].rect.left - 43    
                    player.velx = 0

        #Colisao do jogador com os inimigos            
        dano = pygame.sprite.spritecollide(player, inimigos, False)
        if dano:
            pygame.mixer.Sound('damage.wav').play()
            hp = hp - 0.5

        #Colisao do jogador com o inimigo especial            
        dano2 = pygame.sprite.spritecollide(player, inimigo2, False)
        if dano2:
            pygame.mixer.Sound('damage.wav').play()
            hp = hp - 2.0
            

        #Colisao para meus itens de pontuacao
        points = pygame.sprite.spritecollide(player, items, False)
        for ponto in points:
            pygame.mixer.Sound('item.wav').play()
            ponto.rect.x = random.randrange(1224, 1324)
            ponto.rect.y = random.randrange(0, 800)
            score += 1

        #Colisao para meu iten especial
        pointSpecial = pygame.sprite.spritecollide(player, special, False)
        for ponto in pointSpecial:
            pygame.mixer.Sound('special.wav').play()
            ponto.rect.x = 6000
            ponto.rect.y = random.randrange(0, 800)
            score += 5
            

        
        #Draw/Render
        #screen.fill(BLACK)
            
        #Desenhando meu parallax para a dificuldade maxima
        if uded == True:
            screen.blit(bottomded, [0, 0])

            #Atualizando detalhes do fundo do cenario
            for item in detalhe_list:
                item[1] -= 2
                pygame.draw.circle(screen, BLACK, item, 5)
                if item[1] <200:
                    item[1] = random.randrange(700, 1500)
                    item[0] = random.randrange(1224)
            
            screen.blit(midbottomImage, [mbX, 100])
            screen.blit(midtopImage, [mtX, 200])

            for item in rain_list:
                item[1] += 5
                item[0] -= 2
                pygame.draw.circle(screen, WHITE, item, 1)
                if item[1] > 840:
                    item[1] = random.randrange(-20, -5)
                    item[0] = random.randrange(200, 1500)

        #Desenhando meu parallax para as outras dificuldades    
        else:
            #mbX = X do midbottom/ mtX = X do midtop/ tX = X do top
            screen.blit(bottomImage, [0, 0])
            screen.blit(midbottomImage, [mbX, 100])
            screen.blit(midtopImage, [mtX, 200])
            screen.blit(topImage, [tX, 340])
        
        if uded == True:
            all_spritesB.draw(screen)
            all_sprites.draw(screen)
        else: all_sprites.draw(screen)

        #Chamando a funcao que mostra a vida do jogador
        Vida(hp)

        #Chamando minha funcao de pontuacao
        if dif == 1:
            Score(score, highA)
        elif dif == 2:
            Score(score, highB)
        elif dif == 3:
            Score(score, highC)
        elif dif == 4:
            Score(score, highD)

        #Flip do display
        pygame.display.flip()        


    




    
    















