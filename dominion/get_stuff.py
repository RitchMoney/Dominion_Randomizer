import random

def get_sets(x):
    sets = []
    #integrate with Flask Here
    #append each set dictionary to sets list
    return sets

# Takes list of sets and returns a card
def get_a_card(lst):
    set = random.choice(lst)
    card_name = random.choice(set.keys())
    return card_name

