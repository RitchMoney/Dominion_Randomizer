#This is the command-line application for ingest of dominion data. run as "python3 -m ingest.ingest_tool" from root of project

import argparse
from ingest.get_expansions import get_expansions
from ingest.retrieve_card_data import get_card_data, get_kcard_links
from ingest.serialize_data import serialize, unserialize

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Welcome to the DominionData ingest tool!')
  parser.add_argument('-e','--get-expansion-data', action='store_true', help='Download Expansions data')
  parser.add_argument('-E','--show-expansions', action='store_true', help='Show the stored list of sets')
  parser.add_argument('-C','--show-cards', help='Show the cards for a specified expansion')
  parser.add_argument('-l','--long', action='store_true', help='long output for show commands')
  parser.add_argument('-c','--get-card-data', nargs="*", help='Download card data for specified expansions, or all if no argument is provided')
  parser.add_argument('-d', action='store_true')
  args = parser.parse_args()
  if args.d:
    print(args)
    exit()

  if args.get_expansion_data: 
    print('get_expansion_data specified. Downloading all Dominion sets.')
    get_expansions(save_output=True)
    print('success')

  if args.get_card_data is not None:
    requested_expansions = args.get_card_data
    expansion_links = unserialize('expansions')
    if requested_expansions == []: requested_expansions = list(expansion_links.keys())  #defualts to all
    print('get_card_data specified. Downloading kingdom cards for sets: {}'.format(requested_expansions))
    for expansion_name in requested_expansions:
      link = expansion_links[expansion_name]
      card_links = get_kcard_links(link)
      print('downloading data for {}: '.format(expansion_name), end='')
      expansion_data = {}
      for card_link in card_links:
        print('.', end='')
        card_data = get_card_data(card_link)
        expansion_data[card_data['name']] = card_data
      print('')
      serialize(expansion_data, 'sets/{}'.format(expansion_name.replace(' ', '_')))



  if args.show_expansions:
    print("Showing stored set list")
    expansions = unserialize('expansions')
    for name, link in expansions.items():
      print('{} ({})'.format(name, link))

  if args.show_cards:
    expansions = args.show_cards
    print("Showing cards for expansion: {}".format(expansions))
    expansion_cards = unserialize('sets/{}'.format(expansions))
    print('there are {} kingdom cards in this set:'.format(len(expansion_cards)))
    for card in expansion_cards.values():
      if args.long:
        print(list(card.values()))
      else: print(card['name'], end=", ")
      print()
  #print('expansions:\n\n', expansions)