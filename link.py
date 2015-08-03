import argparse
import json

from listing import Listing
from product import Product
from tokens import (
  token_distance,
  tokenize_and_normalize,
  idf_of_all_tokens
)

def link(prod_file, list_file, out_file):
  products = []
  listings = []

  with open(prod_file, 'r') as f:
    for line in f:
      products.append(Product(line))

  with open(list_file, 'r') as f:
    for line in f:
      listings.append(Listing(line))

  idf_tokens = idf_of_all_tokens(products, listings)
  product_list_links = {p.product_name: [] for p in products}
  count = 0
  for listing in listings:
    for product in products:
      distance = token_distance(product, listing, idf_tokens)
      if distance > 0.7:
        listing.possible_products.append((product.product_name, distance))
    if len(listing.possible_products) > 0:
      listing.possible_products.sort(key=lambda x: x[1], reverse=True)
      top_product, top_distance = listing.possible_products[0]
      if (len(listing.possible_products) > 1 and 
            listing.possible_products[0][1] == listing.possible_products[1][1]):
        # if top two distances are equal, do not link to reduce mismatch
        # TODO: find distance of complex tokens and use it as tie breaker
        continue
      count = count + 1
      product_list_links[top_product].append(listing.l_dict)
    # TODO: filter out listings with price converted to USD is an outlier

  print('Matched Links: %d' % (count))

  with open(out_file, 'w') as f:
    for key, val in product_list_links.iteritems():
      f.write(json.dumps({
        'product_name': key,
        'listings': val,
      }) + '\n')
