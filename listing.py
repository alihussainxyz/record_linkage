import json
from tokens import tokenize_and_normalize

class Listing:
  def __init__(self, l_json):
    l_json = l_json.lower()
    self.l_dict = json.loads(l_json)
    self.title = self.l_dict.get('title', '')
    self.manufacturer = self.l_dict.get('manufacturer', '')
    self.currency = self.l_dict.get('currency', '')
    self.price = self.l_dict.get('price', '')
    self.tokens = tokenize_and_normalize(self.title)
    #TODO: add complex tokens separately i.e. different combinations
    self.possible_products = []

  def __repr__(self):
    return json.dumps(self.l_dict)
