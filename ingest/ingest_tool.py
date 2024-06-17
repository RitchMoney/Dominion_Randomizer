#This is the command-line application for ingest of dominion data. run as "python3 -m ingest.ingest_tool" from root of project

import argparse
from ingest.get_expansions import get_expansions
from ingest.serialize_data import unserialize

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Welcome to the DominionData ingest tool!')
  parser.add_argument('-e','--get-expansion-data', default=False, action='store_true', help='Download Expansions data', required=False)
  parser.add_argument('-s','--show', choices=['expansions', 'cards'], nargs="+", help='Show stored values for the provided choices', required=False)

  args = parser.parse_args()
  
  if args.get_expansion_data: 
    print('get_expansion_data specified. Downloading all Dominion sets.')
    get_expansions(save_output=True)
    print('success')

  for option in args.show:
    print("Showing stored data for: ", option)
    print(unserialize(option))
  #print('expansions:\n\n', expansions)