import pygame
import pygame.freetype
from card import Card
pygame.init()

screen = pygame.display.set_mode([370, 370])
pygame.display.set_caption("Kanji Match")
font = pygame.freetype.Font('JF-Dot-Izumi16.ttf', 30)

cards = []

for i in range(6):
    for j in range(6):
        cards.append(Card(i, j))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((143, 130, 79))

    for card in cards:
        card.draw(screen, font)

    pygame.display.flip()

pygame.quit()