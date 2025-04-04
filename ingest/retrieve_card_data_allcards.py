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
            for child in td.decendants: # iterate through all tags and strings below
                if isinstance(child, NavigableString): #looking for plaintext to grab
                    row_data[i].append(child.get_text(),' ')
                elif child.name == 'hr': #looking for deviders to grab
                    row_data[i].append('// ')
                elif child.name == 'span' or child.name == 'a': #looking for images to replace
                    text = convert_images_to_text(child)
                    if text != None:
                        row_data[i].append(text,' ')
        data.append(row_data)

    return data

# remove links and keep just text 


# 
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


if __name__ == main:

    cardtable = get_table(all_cards_webpage)

    all_cards_webpage = 'https://wiki.dominionstrategy.com/index.php/List_of_cards'