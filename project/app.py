import pandas as pd
import requests


def write_data(compound):
    api_endpoint = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/{}'.format(compound)
    data = requests.get(api_endpoint)
    res1 = data.json()
    keys = ['name', 'formula', 'inchi', 'inchi_key', 'smiles']
    dict2 = {x: res1[compound][0][x] for x in keys}
    dict2['cross_links_count'] = len(res1[compound][0]['cross_links'])
    dict2['compound'] = compound
    return dict2


print(write_data('STI'))

