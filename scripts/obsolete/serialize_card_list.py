#run from parent directory with:
#  python3 -m scripts.serialize_card_list

from dominion import util
if __name__ == '__main__':
  cards = util.parse_cards_file()
  util.pickle_obj(cards, 'dominion_data/pickle/cards.pkl')