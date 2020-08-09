import pygame
class Card:

    x = 0
    y = 0
    color = (200, 200, 55)
    SIZE = 50
    SPACING = 10

    def __init__(self, x, y):
        self.x = x * (self.SIZE + self.SPACING) + self.SPACING
        self.y = y * (self.SIZE + self.SPACING) + self.SPACING

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.SIZE, self.SIZE), 0)
        font.render_to(screen, (self.x, self.y), "命ご", (0, 0, 0))