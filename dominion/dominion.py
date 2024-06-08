class Card:
  name : str
  
  def __init__(self, name):
    self.name = name

  @staticmethod
  def get_arbitrary_card():
    return Card('Cellar')
  
class Kingdom:
  cards : list
  max_size : int = 10
  
  def __init__(self):
   self.generate()
  
  def add_card(self, card : Card):
    self.cards.append(card)

  def get_cards(self) -> list:
    return self.cards
  
  def generate(self):
    cards = []
    while (len(cards) < self.max_size):
        #TODO expand to replace 'get_arbitrary_card'
        cards.append(Card.get_arbitrary_card())
    self.cards = cards