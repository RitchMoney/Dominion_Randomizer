import unittest

from dominion_data.util import get_loaded_expansion_names

#tests the basic dominion game package, which contains game-related objects
class DominionDataTests(unittest.TestCase):
  def test_get_loaded_expansion_list(self):
    expansions = get_loaded_expansion_names()
    print(expansions)


