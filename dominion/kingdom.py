import random
from dominion.util import get_random_card
from dominion.card import Card
from dominion_data.util import get_expansion_data

class Kingdom:
  cards : list
  max_size : int = 10
  included_expansions : list

  def __init__(self):
    pass

  def add_card(self, card : Card):
    self.cards.append(card)

  def get_cards(self) -> list:
    return self.cards
  
  def generate(self):
    cards = []
    candidate_cards = []
    for expansion in self.included_expansions:
      expansion_cards = get_expansion_data(expansion)
      for card_data in expansion_cards:
        candidate_cards.append(Card.from_card_data(card_data))
    while (len(cards) < self.max_size):
        random_card = random.choice(candidate_cards)
        random_card = candidate_cards.pop(random.randrange(len(candidate_cards)))
        cards.append(random_card)
    self.cards = cards