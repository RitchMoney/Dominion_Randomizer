import pandas as pd
import requests
from bs4 import BeautifulSoup

from ingest.serialize_data import serialize

#uses Pandas library to pars the html tables into Dataframes, and then grabs a list of expansion names. It also appends 'Base' manually.
#credit: https://stackoverflow.com/questions/56757261/extract-href-using-pandas-read-html
def get_expansions(save_output=False, expansions_page='https://wiki.dominionstrategy.com/index.php/Expansions') -> list:
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
        link = None
      if link: links.append(link)
  #add the links into the original dataframe from pandas parsing
  df['Link'] = links
  df = df.reset_index()  # make sure indexes pair with number of rows

  little_dict = {}
  for index, row in df.iterrows():
    little_dict[row['Expansion']] = row['Link']
  little_dict['Base'] = "/index.php/Base"   #manually add Base, its not on the list.

  if save_output: serialize(little_dict, 'expansions')
  return little_dict
