import pygame
from card import Card
pygame.init()

screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption("Kanji Match")

cards = []
cardSpacing = 50

for i in range(6):
    for j in range(6):
        cards.append(Card(i * cardSpacing, j * cardSpacing))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for card in cards:
        card.draw(screen)

    pygame.display.flip()

pygame.quit()