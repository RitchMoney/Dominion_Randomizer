class Card:
  name : str
  
  def __init__(self, name):
    self.name = name
    self.img = self.set_image()

  def __str__(self):
    return "{} [Card] - {}".format(self.name, self.img)
  
  def set_image(self):
    img_dir = '/static/card_img/'
    name = self.name.replace(" ", "_")
    return '{}{}Digital.jpg'.format(img_dir, name)
  
  @staticmethod
  def from_card_data (card_data : dict):
    print(card_data)
    return Card(name=card_data['name'])