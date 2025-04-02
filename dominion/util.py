from dominion.card import Card
import pickle 
import random

def get_random_card(candidate_cards : list[str] = None) -> Card:
  if candidate_cards is None:
    candidate_cards = get_from_pickle('card_names')
  try:
    card_name = random.choice(candidate_cards)
  except:
    return
  return Card(card_name)

def get_expansion_card_names(expansion_name : str) -> dict:
  expansion_data = get_from_pickle('sets/{}'.format(expansion_name))
  return list(expansion_data.keys())

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

