import json
import random
import copy
class KanjiData:

    def __init__(self):
        with open("data/kanji.json", "r", encoding="utf-8") as file:
            self.data = json.load(file)
            self.resetDeck()

    def resetDeck(self):
        self.deck = copy.deepcopy(self.data)
    
    def getCard(self):
        difficulty = "kanji"
        card = random.choice(list(self.deck[difficulty].items()))

        (key, value) = card

        for k, v in list(self.deck[difficulty].items()):
            if v == value:
                self.deck[difficulty].pop(k)

        if len(self.deck[difficulty]) == 0:
            self.resetDeck()

        return card