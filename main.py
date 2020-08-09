import pygame
import pygame.freetype
import random
from card import Card
from kanjiData import KanjiData
pygame.init()

screen = pygame.display.set_mode([370, 370])
pygame.display.set_caption("Kanji Match")
clock = pygame.time.Clock()
font = pygame.freetype.Font("data/Boku2-Bold.otf", 40)
kanjiData = KanjiData()

cards = []
rowWidth = 6
selectedCard = None

def init():
    for i in range(rowWidth):
        for j in range(rowWidth):
            cards.append(Card(i, j))

    for i in range(len(cards)):
        if i % 2 == 0:
            (key, value) = kanjiData.getCard()
            cards[i].text = key
        else:
            cards[i].text = value
        cards[i].id = int(i / 2)

    for i in range(len(cards)):
        cardA = random.choice(cards)
        cardB = random.choice(cards)
        cardA.x, cardB.x = cardB.x, cardA.x
        cardA.y, cardB.y = cardB.y, cardA.y

init()
    

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if selectedCard != None:
                    for card in cards:
                        if card.hovered:
                            if not card.selected:
                                if card.id == selectedCard.id:
                                    card.destroy()
                                    selectedCard.destroy()
                                else:
                                    card.error()
                                    selectedCard.error()
                            selectedCard.selected = False
                            selectedCard = None
                            break
                else:
                    for card in cards:
                        if card.hovered:
                            card.selected = True
                            selectedCard = card
                            break
            elif event.button == 3:
                selectedCard.selected = False
                selectedCard = None

    screen.fill((91, 117, 194))

    for card in cards:
        card.update()
        card.checkHover()
        card.draw(screen, font)

    for card in cards:
        if card.destructionTimer >= card.maxDestructionTimer:
            cards.remove(card)
    
    if len(cards) == 0:
        init()

    pygame.display.flip()
    clock.tick(40)

pygame.quit()