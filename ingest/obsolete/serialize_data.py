import pickle
import os 

def serialize(data : any, relative_path : str, base_path='dominion_data/pickle/') -> None:
   path = '{}{}.pkl'.format(base_path, relative_path)
   os.makedirs(os.path.dirname(path), exist_ok=True) #creates dirs if needed
   with open (path, 'wb') as file:
    pickle.dump(data, file)

def unserialize(pickle_name : str, base_path='dominion_data/pickle/') -> any:
   path = '{}{}.pkl'.format(base_path, pickle_name)
   with open (path.format(path), 'rb') as f:
    return pickle.load(f)
