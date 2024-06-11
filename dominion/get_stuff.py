import random
from card import Card

def get_expansions(sets_dict): 
    #pull pickle (dict of sets each a dict of cards each a dict of info)
    #integrate with Flask user input here
    #delete sets from pkl dict that were not selected
    return sets_dict

# Takes dict of sets and returns a random card 
def get_a_card(dct):
    expansion = random.choice(dct)
    card_dict = random.choice(expansion)
    card_obj = Card(card_dict)
    return card_obj
