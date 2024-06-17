import pickle

def serialize(data : any, relative_path : str, base_path='dominion_data/pickle/') -> None:
   path = '{}{}'.format(base_path, relative_path)
   with open (path, 'wb') as file:
    pickle.dump(data, file)

def unserialize(pickle_name : str, base_path='dominion_data/pickle/') -> any:
   path = '{}{}'.format(base_path, pickle_name)
   with open (path.format(path), 'rb') as f:
    return pickle.load(f)
