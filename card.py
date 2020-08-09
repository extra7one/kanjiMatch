import pygame
class Card:

    x = 0
    y = 0
    color = (200, 200, 55)
    hoveredColor = (225, 225, 75)
    selectedColor = (225, 225, 150)
    hovered = False
    text = ""
    id = 0
    selected = False
    destroyed = False
    destructionTimer = 0

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

        if self.destroyed:
            surface.set_alpha(255 - (255 * self.destructionTimer / 50))

        color = self.color
        if self.selected or self.destroyed:
            color = self.selectedColor
        elif self.hovered:
            color = self.hoveredColor

        pygame.draw.rect(surface, color, (0, 0, self.SIZE, self.SIZE), 0)
        font.render_to(surface, (5, 5), self.text, (0, 0, 0))

        screen.blit(surface, (self.x, self.y))

    def update(self):
        if self.destroyed:
           self.destructionTimer += 1

    def setText(self, text):
        self.text = text

    def setID(self, id):
        self.id = id

    def setSelected(self, selected):
        self.selected = selected

    def destroy(self):
        self.destroyed = True
    
    def isHovered(self):
        return self.hovered

    def isSelected(self):
        return self.selected

    def getID(self):
        return self.id

    def getDestructionTimer(self):
        return self.destructionTimer