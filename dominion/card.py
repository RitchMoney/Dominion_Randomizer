class Card:
  name : str
  
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return "{} [Card]".format(self.name)