import pygame
from random import randint
class Card:

    x = 0
    y = 0
    color = (135, 166, 222)
    hoveredColor = (129, 179, 240)
    selectedColor = (110, 194, 255)
    errorColor = (255, 100, 100)
    correctColor = (100, 255, 100)
    hovered = False
    text = ""
    id = 0
    selected = False
    destroyed = False
    destructionTimer = 0
    maxDestructionTimer = 25
    errorTimer = 0
    maxErrorTimer = 15

    SIZE = 50
    SPACING = 10

    def __init__(self, x, y):
        self.x = x * (self.SIZE + self.SPACING) + self.SPACING
        self.y = y * (self.SIZE + self.SPACING) + self.SPACING

    def checkHover(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX >= self.x and mouseX < self.x + self.SIZE and mouseY >= self.y and mouseY < self.y + self.SIZE and not self.destroyed:
            self.hovered = True
        else:
            self.hovered = False

    def draw(self, screen, font):

        surface = pygame.Surface((self.SIZE, self.SIZE))
        posX = 0
        posY = 0

        if self.destroyed:
            surface.set_alpha(255 - (255 * self.destructionTimer / self.maxDestructionTimer))

        color = self.color
        if self.selected:
            color = self.selectedColor
        elif self.destroyed:
            color = self.correctColor
        elif self.errorTimer > 0:
            color = self.errorColor
            posX += randint(-3, 3)
            posY += randint(-3, 3)
        elif self.hovered:
            color = self.hoveredColor

        pygame.draw.rect(surface, color, (0, 0, self.SIZE, self.SIZE), 0)
        textSurface, textRect = font.render(self.text)
        font.render_to(surface, (posX + self.SIZE / 2 - textRect.width / 2, posY + self.SIZE / 2 - textRect.height / 2), self.text, (0, 0, 0))

        screen.blit(surface, (self.x, self.y))

    def update(self):
        if self.destroyed:
           self.destructionTimer += 1
        if self.errorTimer > 0:
            self.errorTimer -= 1

    def destroy(self):
        self.destroyed = True

    def error(self):
        self.errorTimer = self.maxErrorTimer