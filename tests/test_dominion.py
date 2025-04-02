import unittest
from dominion.kingdom import Kingdom, Card
import dominion.util as util

#tests the basic dominion game package, which contains game-related objects
class DominionTests(unittest.TestCase):
  def test_create_kingdom(self):
    k = Kingdom()
    assert(not hasattr(k, 'cards'))
  def test_generate_kingdom(self):
    k = Kingdom()
    k.generate_kingdom()
    assert(k.cards == [None, None, None, None, None, None, None, None, None, None])

    k = Kingdom(included_expansions=["Intrigue"])
    k.generate_kingdom()
    print(k.cards)
    unique_card_names = set([card.name for card in k.cards])
    assert(len(unique_card_names) == 10) #prove there are no duplicates


class UtilTests(unittest.TestCase):
  def test_get_expansion_cards(self):
    expansion_name = 'Intrigue'
    expansion_cards = util.get_expansion_card_names(expansion_name)
    assert expansion_cards == ['Courtyard', 'Lurker', 'Pawn', 'Masquerade', 'Shanty Town', 
                               'Steward', 'Swindler', 'Wishing Well', 'Baron', 'Bridge', 'Conspirator', 
                               'Diplomat', 'Ironworks', 'Mill', 'Mining Village', 'Secret Passage', 'Courtier', 
                               'Duke', 'Minion', 'Patrol', 'Replace', 'Torturer', 'Trading Post', 'Upgrade', 
                               'Farm', 'Nobles']
  def test_get_random_card(self):
    random_card = util.get_random_card()
    print(random_card)
    intrigue_cards = util.get_expansion_card_names('Intrigue')
    random_intrigue_card = util.get_random_card(candidate_cards=intrigue_cards)
    print(random_intrigue_card)
  