#import pandas as pd
import requests
from bs4 import BeautifulSoup

#uses Pandas library to pars the html tables into Dataframes, and then grabs a list of expansion names. It also appends 'Base' manually.
#credit: https://stackoverflow.com/questions/56757261/extract-href-using-pandas-read-html
def get_expansions() -> list:
  expansions_page='https://wiki.dominionstrategy.com/index.php/Expansions'

  #uses pandas to parse the html to grab all tables, and then save the first table (which is the expansions) to a DataFrame
  df = pd.read_html(expansions_page)[0]

  #grabs the web page again, this time using the requests library and then parses it with the BeautifulSoup parser.
  #the purpose of this section is to get the href links (links to each expansion's page). Pandas just grabs text only.
  response = requests.get(expansions_page)
  soup = BeautifulSoup(response.text, 'html.parser')
  table = soup.find('table')

  #parse the page to find the links associated with each expansion
  links = []
  for tr in table.findAll("tr"):
      try:
        link = tr.find('a')['href']
      except:
        link = Nonecard_name = soup.select_one('body h1').get_text()
      if link: links.append(link)

  #add the links into the original dataframe from pandas parsing
  df['Link'] = links
  df = df.reset_index()  # make sure indexes pair with number of rows

  little_dict = {}
  for index, row in df.iterrows():
    little_dict[row['Expansion']] = row['Link']
  #manually add Base, its not on the list.
  little_dict['Base'] = "/index.php/Base"
  return little_dict

#takse soup and id of heading - returns list of all relative links in next sibling 
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
