from dominion.card import Card
import pickle 
import random

def get_random_card() -> Card:
  card_list = get_from_pickle('cards')
  card_name = random.choice(card_list)
  return Card(card_name)

def get_from_pickle(pickle_name : str, path : str = 'dominion_data/pickle/{}.pkl'):
  with open (path.format(pickle_name), 'rb') as f:
    return pickle.load(f)

def parse_cards_file(card_file = 'dominion_data/card_list'):
  with open (card_file) as cards_file:
    cards = [card.strip() for card in cards_file.readlines()]
  return cards

def pickle_obj(obj : list, filename) -> None:
  with open (filename, 'wb') as file:
    pickle.dump(obj, file)

