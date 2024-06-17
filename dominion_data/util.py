from os import walk

from ingest.serialize_data import unserialize

def get_loaded_expansion_names():
  path = 'dominion_data/pickle/sets/'
  f = []
  for (dirpath, dirnames, filenames) in walk(path):
      f.extend(filenames)
  return [filename.split('.')[0] for filename in filenames]

def get_expansion_data(expansion_name: str):
  expansion = unserialize('sets/{}'.format(expansion_name))
  cards = expansion.values()
  return cards