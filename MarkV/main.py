import pygame
from pygame.locals import *

# Inicializa os módulos do pygame
pygame.init()

screen_width = 800  # Largura da tela do jogo
screen_height = 600  # Altura da tela do jogo
screen = pygame.display.set_mode((screen_width, screen_height))  # Define o tamanho da tela do jogo
pygame.display.set_caption("Jogo da Nave Espacial")

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self, name):
        super(naveEspacial, self).__init__()
        self.name = name
        self.alive = True
        self.position = pygame.math.Vector2(screen_width // 2, screen_height // 2)
        self.direction = 0
        self.speed = 5
        self.max_speed = 20 
        self.default_speed = 5  
        self.shield = 100
        self.energy = 100
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        keys = pygame.key.get_pressed()


        if keys[K_n]:
            if self.speed <= self.max_speed:
                self.speed = self.speed + 1

        if keys[K_m]:
            if self.speed != self.default_speed:
                self.speed = self.speed - 1

        # Movimentação
        if keys[K_LEFT]:
            self.position.x -= self.speed

        if keys[K_RIGHT]:
            self.position.x += self.speed

        if keys[K_UP]:
            self.position.y -= self.speed

        if keys[K_DOWN]:
            self.position.y += self.speed

        # Atualiza a posição do retângulo da nave
        self.rect.center = self.position

def main():
    nave = naveEspacial("Falcon")
    all_sprites = pygame.sprite.Group()
    all_sprites.add(nave)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        all_sprites.update()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
