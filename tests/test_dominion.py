import unittest
from dominion.kingdom import Kingdom
import dominion.util as util

#tests the basic dominion game package, which contains game-related objects
class DominionTests(unittest.TestCase):
  def test_create_kingdom(self):
    k = Kingdom()
    assert(not hasattr(k, 'cards'))
  def test_generate_kingdom(self):
    k = Kingdom()
    k.generate()
    #[print(c.name) for c in k.cards]
    assert(len(k.cards) > 0)

class UtilTests(unittest.TestCase):
  def test_get_random_card(self):
    card = util.get_random_card()
    print(card)
