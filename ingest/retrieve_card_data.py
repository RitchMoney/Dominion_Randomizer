import requests
from bs4 import BeautifulSoup

from ingest.get_expansions import get_expansions

#take soup and id of heading - returns list of all relative links in next sibling 
# id of the heading lives in the child of h3 tag so we gotta traverse the tree a bit.
# should work for any section of cards, which will be useful as we start dealign with non kingdom cards
def get_card_links(soup,heading_id : str):
  find_me = "{}{}".format("#", heading_id)
  heading = soup.select_one(find_me).parent
  section = heading.next_sibling.next_sibling #https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=find_next_sibling#going-sideways
  card_links = []
  for a in section.select('a[href]'):
    card_links.append(a['href'])

  return card_links


#takes the relative url to an expansion's wiki page as the argument, and generates a dictionary containing each kingdom card.
def get_kingdom_cards_for_expansion(expansion_page : str):
  base_url = 'https://wiki.dominionstrategy.com'
  full_url = '{}{}'.format(base_url, expansion_page)
  expansion = {}
  response = requests.get(full_url)
  soup = BeautifulSoup(response.text, 'html.parser')
  card_links = get_card_links(soup, 'Kingdom_cards')
  
  for link in card_links:
    #get and parse page
    card_url = '{}{}'.format(base_url, link)
    card_response = requests.get(card_url) 
    soup = BeautifulSoup(card_response.text, 'html.parser') 

    #get card name from heading
    card_name = soup.select_one('body h1').get_text(strip=True)

    #get card text from right side table. newline will format it correctly too :3
    for tbl in soup.find_all("table"):
      txt = tbl.get_text("\n", strip = True)
      if "Card text" in txt:
        card_text = txt.split("Card text",1)[1]
        break

    #add elements to dictionary
    expansion[card_name] = {}
    expansion[card_name]['name'] = card_name
    expansion[card_name]['link'] = card_url
    expansion[card_name]['text'] = card_text

  return expansion
  
  #Ritchie, maybe you can implement the funcitonality of this. It'll be a challenge so no sweat if it takes a little bit. Reference the link:
  #https://stackoverflow.com/questions/56757261/extract-href-using-pandas-read-html


#takes a list of expansions, and generates dict of kingdom cards for all expansions.
def get_kingdom_cards_for_expansion_list(expansions : dict) -> dict:
  big_dict = {}
  for expansion_name, link in expansions.items():
    big_dict[expansion_name] = get_kingdom_cards_for_expansion(link)
  return

if __name__ == '__main__':
  expansions = get_expansions()
  get_kingdom_cards_for_expansion_list(expansions)
