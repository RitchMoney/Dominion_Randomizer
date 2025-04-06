import requests
from bs4 import Tag, NavigableString, BeautifulSoup
from dominion import util

# takes all cards webpage and returns a nested list of strings for each cell in card table.
def get_table(webpage: str) ->  list:
    response = requests.get(webpage)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table') #make sure this pulls proper table
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        for i, td in enumerate(columns):
            cell = ''
            if not td.descendants:
                continue
            for child in td.descendants: # iterate through all tags and strings below        -\
                if isinstance(child, NavigableString): #looking for plaintext to grab         \
                    cell += child.get_text() + ' ' #                                 \
import requests
from bs4 import Tag, NavigableString, BeautifulSoup
import csv

# takes all cards webpage and returns a nested list of strings for each cell in card table.
def get_table(webpage: str) ->  list:
    response = requests.get(webpage)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    table = soup.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        row_data = []
        for td in columns:
            cell = ''
            if not td.descendants:
                continue
            for child in td.descendants: # iterate through all tags and strings below 
                if isinstance(child, NavigableString): #looking for plaintext to grab
                    cell += child.get_text() + ' '
                elif child.name == 'hr': #looking for deviders to grab
                    cell += '// '
                elif child.name == 'span' or child.name == 'a':
                    text = convert_images_to_text(child)
                    if text != None:
                        cell += text + ' '
            row_data.append(cell.strip())
        if row_data:
            data.append(row_data)

    return data

def convert_images_to_text(bs_element : Tag) -> str:
    if bs_element.has_attr('class') and bs_element['class'][0] == 'coin-icon':
        image = bs_element.find('img')
        if image['alt'] != 'P': #potions are coin icons for some reason :(
            return image['alt']
    
    if bs_element.has_attr('title') and bs_element['title'] == 'Victory point':
        return 'VP'
    
    if bs_element.has_attr('title') and bs_element['title'] == 'Potion':
        return 'POTION'
    
    if bs_element.has_attr('title') and bs_element['title'] == 'Debt':
        image = bs_element.find('img')
        return image['alt']

    return None

def table_to_dict(table_of_cards: list[list[str]]) -> dict:
    expansions = {}
    for card in table_of_cards:
        current_expansion = card[1]
        card_name = card[0]
        if current_expansion not in expansions:
            expansions[current_expansion] = {}
        expansions[current_expansion][card_name] = {
          "name": card[0],
          "expansion": card[1],
          "types": card[2], # fix so is a list instead of string
          "cost": card[3], 
          "text": card[4],
          "actions": card[5], # includes villagers
          "cards": card[6], # draw or discard
          "buys": card[7],
          "coins": card[8], # includes coffers
          "trash": card[9],
          "exile": card[10],
          "junk": card[11],
          "gain": card[12],
          "vp": card[13]
        }
    return expansions    


if __name__ == '__main__':
    all_cards_webpage = 'https://wiki.dominionstrategy.com/index.php/List_of_cards'
    
    cardtable = get_table(all_cards_webpage)

    # contains dict of expansions, each a dict of all cards in that expansion, each a dict of card info.
    master_dictionary = table_to_dict(cardtable) 

    util.pickle_obj(master_dictionary, 'dominion_data/pickle/all_cards.pkl')