import pygame
import pygame.freetype
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
                cards[i].setText(key)
            else:
                cards[i].setText(value)
            cards[i].setID(int(i / 2))

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
                        if card.isHovered() and not card.isSelected():
                            if card.getID() == selectedCard.getID():
                                card.destroy()
                                selectedCard.destroy()
                            selectedCard.setSelected(False)
                            selectedCard = None
                            break
                else:
                    for card in cards:
                        if card.isHovered():
                            card.setSelected(True)
                            selectedCard = card
                            break

    screen.fill((143, 130, 79))

    for card in cards:
        card.update()
        card.checkHover()
        card.draw(screen, font)

    for card in cards:
        if card.getDestructionTimer() >= 50:
            cards.remove(card)
    
    if len(cards) == 0:
        init()

    pygame.display.flip()
    clock.tick(40)

pygame.quit()