from dominion.util import get_random_card
from dominion.card import Card

class Kingdom:
  cards : list
  max_size : int = 10
  
  def __init__(self):
    pass

  def add_card(self, card : Card):
    self.cards.append(card)

  def get_cards(self) -> list:
    return self.cards
  
  def generate(self):
    cards = []
    while (len(cards) < self.max_size):
        cards.append(get_random_card())
    self.cards = cards