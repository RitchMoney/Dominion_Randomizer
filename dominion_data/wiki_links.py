import pandas as pd


def get_expansion_pages():
  expansions_page='https://wiki.dominionstrategy.com/index.php/Expansions'
  dfs = pd.read_html(expansions_page)
  df = dfs[0]  # pd.read_html reads in all tables and returns a list of DataFrames
  print('df', df)

if __name__ == '__main__':
  get_expansion_pages()