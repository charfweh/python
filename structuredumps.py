# Different python packages to dump data structures and create cache.

# Namely: Json and Pickle.

import json
import pickle

data = {
    'red': "#FF0000",
    'green': "#00FF00",
    'blue': "#0000FF",
}

# Dumping the dictionary

pickle.dump(data, open("Hexcode.pkl", "wb"))         # Pickle

json.dump(data, open("Hexcode.json", 'w'))          # Json


# Loading the files

pickle_file = pickle.load(open("Hexcode.pkl", 'rb'))

with open("Hexcode.json", 'r') as f:
    json_file = f

