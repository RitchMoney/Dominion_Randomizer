from dominion.util import get_random_card
import get_stuff
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
    sets = get_stuff.get_sets()
    
    cards = []
    while (len(cards) < self.max_size):
      card = get_stuff.get_a_card()

      # call filtering here

      cards.append(card)
    self.cards = cards