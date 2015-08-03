import json
from tokens import tokenize_and_normalize

class Product:
  def __init__(self, p_json):
    p_json = p_json.lower()
    p_dict = json.loads(p_json)
    self.product_name = p_dict.get('product_name', '')
    self.manufacturer = p_dict.get('manufacturer', '')
    self.model = p_dict.get('model', '')
    self.family = p_dict.get('family', '')
    self.announce_date = p_dict.get('announce_date', '')
    self.tokens = tokenize_and_normalize(self.product_name)
    #TODO: add complex tokens separately i.e. different combinations

  def __repr__(self):
    return self.product_name
