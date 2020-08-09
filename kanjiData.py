import json
import random
class KanjiData:

    def __init__(self):
        with open("data/kanji.json", "r") as file:
            self.data = json.load(file)
            self.resetDeck()

    def resetDeck(self):
        self.deck = self.data
    
    def getCard(self):
        difficulty = "easy"
        card = random.choice(list(self.deck[difficulty].items()))
        return card