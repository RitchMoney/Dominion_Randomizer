import requests
from bs4 import BeautifulSoup as bs
import csv

all_cards_webpage = 'https://wiki.dominionstrategy.com/index.php/List_of_cards'

# takes all cards webpage and returns a nested list of BeautifulSoup elements
def get_table(webpage: str) ->  list:
    response = requests.get(webpage)
    soup = bs(response.text, 'html.parser')
    
    data = []
    table = soup.find('table') #make sure this pulls proper table
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        row_data = []
        for td in columns:
            row_data.append(td)
        data.append(row_data)

    return data

# remove links and keep just text 


# convert coin images to plaintext
def convert_coins_to_text(bs_element) -> str:
    coin = bs_element.find('span', class_="coin-icon")
    if coin != None:
        image = coin.find('img')
        return image['alt']
    else:
        return None

def convert_vp_to_text(bs_element) -> str:
    a = bs_element.find('a', title="Victory point")
    if a != None:
        return 'VP'
    else:
        return None


# list = get_table(all_cards_webpage)




# test converting coin image
test_data = '<span style="white-space: nowrap;">3 <span typeof="mw:File"><a href="/index.php/Victory_point" title="Victory point"><img alt="VP" src="/images/thumb/9/92/VP.png/14px-VP.png" decoding="async" loading="lazy" width="14" height="16" class="mw-file-element" srcset="/images/thumb/9/92/VP.png/21px-VP.png 1.5x, /images/thumb/9/92/VP.png/28px-VP.png 2x" data-file-width="461" data-file-height="512"></a></span></span>'
soup = bs(test_data, 'html.parser')
print(convert_vp_to_text(soup))