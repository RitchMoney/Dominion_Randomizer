import dominion.util as util
from dominion.card import Card

class Kingdom:
  cards : list
  max_size : int = 10
  included_expansions : list[str]
  _candidate_card_names : list[str]
  
  def __init__(self, included_expansions : list[str] = []):
    self._set_candidate_card_names(included_expansions)

  def add_card(self, card : Card):
    self.cards.append(card)

  def get_cards(self) -> list:
    return self.cards
  
  def _set_candidate_card_names(self, included_expansions : list[str] = []) -> None:
      self._candidate_card_names = []
      for expansion_name in included_expansions:
        expansion_card_names = util.get_expansion_card_names(expansion_name)
        self._candidate_card_names.extend(expansion_card_names)
  
  def generate_kingdom(self) -> None:
    cards = []
    while (len(cards) < self.max_size):
        selected_card = util.get_random_card(candidate_cards=self._candidate_card_names)
        if selected_card is not None:
          self._candidate_card_names.remove(selected_card.name)
        cards.append(selected_card)

    self.cards = cards