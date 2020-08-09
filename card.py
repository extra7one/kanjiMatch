import pygame
class Card:

    x = 0
    y = 0
    color = (200, 200, 55)
    hoveredColor = (225, 225, 75)
    hovered = False

    SIZE = 50
    SPACING = 10

    def __init__(self, x, y):
        self.x = x * (self.SIZE + self.SPACING) + self.SPACING
        self.y = y * (self.SIZE + self.SPACING) + self.SPACING

    def checkHover(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX >= self.x and mouseX < self.x + self.SIZE and mouseY >= self.y and mouseY < self.y + self.SIZE:
            self.hovered = True
        else:
            self.hovered = False

    def draw(self, screen, font):
        color = self.color
        if self.hovered:
            color = self.hoveredColor
        pygame.draw.rect(screen, color, (self.x, self.y, self.SIZE, self.SIZE), 0)
        font.render_to(screen, (self.x + 5, self.y + 5), "戦", (0, 0, 0))