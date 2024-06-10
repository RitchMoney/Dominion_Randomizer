class Card:
  name : str
  set : str
  data : dict
  
  def __init__(self, dictionary):
    self.name = dictionary["Name"]
    self.set = dictionary["Set"]
    self.data = dictionary
    self.img = self.set_image()

  def __str__(self):
    return "{} [Card] - {}".format(self.name, self.img)
  
  def set_image(self):
    img_dir = '/static/img/'
    name = self.name.replace(" ", "_")
    return '{}{}Digital.jpg'.format(img_dir, self.name)
