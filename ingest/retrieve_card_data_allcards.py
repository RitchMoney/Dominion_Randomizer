import requests
from bs4 import Tag, NavigableString, BeautifulSoup
import csv

# takes all cards webpage and returns a nested list of strings for each cell in card table.
def get_table(webpage: str) ->  list:
    response = requests.get(webpage)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    table = soup.find('table') #make sure this pulls proper table
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        row_data = []
        for i, td in enumerate(columns):
            for child in td.decendants: # iterate through all tags and strings below        -\
                if isinstance(child, NavigableString): #looking for plaintext to grab         \
                    row_data[i].append(child.get_text(),' ') #                                 \
                elif child.name == 'hr': #looking for deviders to grab                          \ 
                    row_data[i].append('// ') #                                                  | Not tested
                elif child.name == 'span' or child.name == 'a': #looking for images to replace  /
                    text = convert_images_to_text(child) #                                     / 
                    if text != None: #                                                        /
                        row_data[i].append(text,' ') #                                      _/
        data.append(row_data)

    return data

def convert_images_to_text(bs_element) -> str:
    coin = bs_element.find('span', class_="coin-icon")
    vp = bs_element.find('a', title="Victory point")
    potion = bs_element.find('a', title="Potion")
    debt = bs_element.find('a', title="debt")
    #
    if coins != None:
        image = coin.find('img')
        return image['alt']
    elif vp != None:
        return 'VP'
    elif potion != None:
        return 'POTION'
    elif debt != None:
        image = debt.find('img')
        return image['alt']
    else:
        return None

#this function is untested 
def table_to_dict(table_of_cards: list[list[str]]) -> dict:
    expansions = {}
    for card in table_of_cards:
        expansions[card[1]][card[0]] = {
          "name": card[0],
          "expansion": card[1],
          "types": [],
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


if __name__ == main:
    cardtable = get_table(all_cards_webpage)

    # contains dict of expansions, each a dict of all cards in that expansion, each a dict of card info.
    master_dictionary = table_to_dict(cardtable) 

    all_cards_webpage = 'https://wiki.dominionstrategy.com/index.php/List_of_cards'