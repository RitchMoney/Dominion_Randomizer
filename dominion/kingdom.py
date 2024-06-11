from dominion.util import get_random_card
import get_stuff
from dominion.card import Card

class Kingdom:
  cards : list
  expansions : list
  max_size : int = 10
  
  def __init__(self):
    pass

  def add_card(self, card : Card):
    self.cards.append(card)

  def get_cards(self) -> list:
    return self.cards
  
  def generate(self):
    expansions = get_stuff.get_expansions()
    
    cards = []
    while (len(cards) < self.max_size):
      card = get_stuff.get_a_card() 

      # call filtering here
      
      cards.append(card)
      del expansions[card.set][card.name] #remove from dict in memory so it is not picked twice
    self.cards = cards