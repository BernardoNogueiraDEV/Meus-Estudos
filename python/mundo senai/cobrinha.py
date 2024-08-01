import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os

largura = 640
altura = 480
pygame.init()
tela = pygame.display.set_mode((largura,altura))
morreu = False
velocidade = 10
x_controle = velocidade
y_controle = 20



lista_corpo = []
comprimento_inicial = 5

pygame.display.set_caption(('cobrinha'))

x_cobra = int(largura / 2 - 40)

y_cobra = int(altura / 2 - 40)

relogio = pygame.time.Clock()

x_maca = int(largura / 4 - 40)

y_maca = int(altura / 4 - 40)

barulho_moeda = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "smb_coin.wav"))

barulho_moeda.set_volume(0.1)

font = pygame.font.SysFont('Impact', 40, False, True)

pontos = 0

def aumentaCobra(lista_corpo):
    for segment in lista_corpo:
        pygame.draw.rect(tela, (0, 255, 0), (segment[0], segment[1], 20, 20))

def reiniciarjogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, x_maca, y_maca, lista_cabeca, lista_corpo, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2 - 40)
    y_cobra = int(altura / 2 - 40)
    x_maca = int(largura / 4 - 40)
    y_maca = int(altura / 4 - 40)
    lista_cabeca = []
    lista_corpo = []
    morreu = False



while True:
    relogio.tick(30)
    
    tela.fill((255,255,255))
    
    mensagem = f'Pontuação: {pontos}'
    
    texto_formatado = font.render(mensagem, False, (0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            elif event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            elif event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

            elif event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
    
    x_cobra += x_controle
    y_cobra += y_controle
    
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 20, 20))
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra, 20, 20))
    
    
    
    if cobra.colliderect(maca):
        x_maca = randint(50,600) 
        y_maca = randint(50,400)
        barulho_moeda.play()
        pontos += 1
        comprimento_inicial += 1
    
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_corpo.append(lista_cabeca)
    
    

    if lista_corpo.count(lista_cabeca) > 1:
        font2 = pygame.font.SysFont('Impact', 20, False, True)
        mensagem = 'Game over, precione R para reiniciar ou apenas feche a janela'
        texto = font2.render(mensagem, True, (0, 0, 0))
        morreu = True
        
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciarjogo()
            tela.blit(texto, (40, 240))
            pygame.display.update()
    
    if x_cobra > largura:
        x_cobra = 0
    elif x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    elif y_cobra < 0:
        y_cobra = altura

    
    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]

    
    aumentaCobra(lista_corpo)
    
    tela.blit(texto_formatado, (400,40))
        
    

    pygame.display.update()