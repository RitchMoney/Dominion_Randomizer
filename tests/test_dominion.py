import unittest
import dominion
from dominion.dominion import Kingdom, Card
import dominion.dominion

#tests the basic dominion game package, which contains game-related objects
class DominionTests(unittest.TestCase):
  def test_create_kingdom(self):
    k = Kingdom()
    assert(k.cards != None)
  def test_generate_kingdom(self):
    k = Kingdom()
    k.generate()
    [print(c.name) for c in k.cards]
    assert(len(k.cards) > 0)

