import pygame
from pygame.locals import *
import os
from sys import exit
import random
from time import sleep
pygame.init()

fps = pygame.time.Clock()
largura = 288
altura = 512
y_bird = altura / 2
velocidade_queda = 2  
x_tubo = largura

pontos = 0
font = pygame.font.SysFont('Impact', 40, False, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Flappy Bird')

background = pygame.image.load(os.path.join(os.path.dirname(__file__),'background-day.png'))
bird = pygame.image.load(os.path.join(os.path.dirname(__file__),'bird.png'))

tubo_baixo = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pipe-green.png'))
tubo_cima = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pipe-green-cima.png'))

def posicao_tubo1():
    tubo_baixo_rect = tela.blit(tubo_baixo, (x_tubo, 450))
    tubo_cima_rect = tela.blit(tubo_cima, (x_tubo, 0))
    return tubo_cima_rect, tubo_baixo_rect

def posicao_tubo2():
    tubo_baixo_rect = tela.blit(tubo_baixo, (x_tubo, 370))
    tubo_cima_rect = tela.blit(tubo_cima, (x_tubo, -80))
    return tubo_cima_rect, tubo_baixo_rect

def posicao_tubo3():
    tubo_baixo_rect = tela.blit(tubo_baixo, (x_tubo, 200))
    tubo_cima_rect = tela.blit(tubo_cima, (x_tubo, -250))
    return tubo_cima_rect, tubo_baixo_rect

def posicao_tubo4():
    tubo_baixo_rect = tela.blit(tubo_baixo, (x_tubo, 400))
    tubo_cima_rect = tela.blit(tubo_cima, (x_tubo, -30))
    return tubo_cima_rect, tubo_baixo_rect

def reiniciarjogo():
    global pontos, y_bird, x_tubo, morreu, passou_tubo
    pontos = 0
    y_bird = altura / 2
    x_tubo = largura
    morreu = False
    passou_tubo = False

funcoes_tubos = [posicao_tubo1, posicao_tubo2, posicao_tubo3, posicao_tubo4]

tubo_atual = None
tubo_cima_rect = None
tubo_baixo_rect = None
morreu = False
passou_tubo = False

while True:
    fps.tick(90)
    tela.blit(background, (0, 0))
    
    mensagem = f'Pontuação: {pontos}'
    texto_formatado = font.render(mensagem, False, (0, 0, 0))
    tela.blit(texto_formatado, (10, 10))

    y_bird += velocidade_queda

    if x_tubo < -tubo_cima.get_width():
        x_tubo = largura
        tubo_atual = random.choice(funcoes_tubos)
        passou_tubo = False
    
    if tubo_atual:
        tubo_cima_rect, tubo_baixo_rect = tubo_atual()
    
    if y_bird > altura - bird.get_height():
        y_bird = altura - bird.get_height()

    bird_rect = pygame.Rect(largura / 2 - bird.get_width() / 2, y_bird, bird.get_width(), bird.get_height())

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                velocidade_queda = -6

    if (tubo_cima_rect and bird_rect.colliderect(tubo_cima_rect)) or (tubo_baixo_rect and bird_rect.colliderect(tubo_baixo_rect)):
        pontos = 0
        font2 = pygame.font.SysFont('Impact', 20, False, True)
        mensagem = 'Precione R para reiniciar'
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

    if not passou_tubo and x_tubo < largura / 2 - bird.get_width() / 2:
        pontos += 1
        passou_tubo = True

    velocidade_queda += 0.2  
    x_tubo -= 2

    tela.blit(bird, (largura / 2 - bird.get_width() / 2, y_bird))
    pygame.display.update()
