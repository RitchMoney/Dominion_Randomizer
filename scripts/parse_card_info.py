#run from parent directory with:
#  python3 -m scripts.parse_card_info
""" 
this will be made obsolete by new scraper
TO DO: 
parse cards into separate dictionaries by set (be careful with 2nd edition sets)
get rid of base treasure, victory, curses, loot, etc.

"""

import csv
from dominion import util
from pathlib import Path


if __name__ == '__main__':
    card_list_path = 'dominion_data/card_list.csv'
    big_dict = {}

    #open csv
    with open(card_list_path, 'r') as csv_file:

        #read csv
        csv_unprocessed = csv.reader(csv_file)
        csv_data = []
        #make into nested
        for line in csv_unprocessed:
            csv_data.append(line)

        column_titles = csv_data[0]

        for row in range(len(csv_data[1:])):

            # fix nesting cases
            if csv_data[row][0] == "":
                continue

            #assign card name to new dictionary key
            key = csv_data[row][0]
            big_dict[key] = {}

            for num in range(len(column_titles)):
                big_dict[key][column_titles[num]] = csv_data[row][num].strip()

    util.pickle_obj(big_dict, 'dominion_data/pickle/card_data.pkl')