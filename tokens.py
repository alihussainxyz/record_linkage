from stop_words import stop_words_set

def tokenize(txt):
  split_chars = ['_', '/', '\\', '(', ')']
  for char in split_chars:
    txt = txt.replace(char, ' ')
  ret_tokens = set()
  tokens = txt.split(' ')
  for token in tokens:
    if '-' in token and len(token) > 4:
      for dash_token in token.split('-'):
        ret_tokens.add(dash_token)
    else:
      ret_tokens.add(token)
  return ret_tokens


def filter_stop_words(token_set):
  return token_set - stop_words_set


def normalize(token_set):
  token_set = token_set - set([''])
  replacements = [('"', 'inch')]
  for old, new in replacements:
    if old in token_set:
      token_set = token_set - set([old])
      token_set = token_set.union(set([new]))
  return token_set


def token_distance(product, listing, idf_all_tokens):
  idf_of_name = 0
  idf_of_intersection = 0
  for token in product.tokens:
    idf_of_name = idf_all_tokens[token] + idf_of_name
  for token in product.tokens.intersection(listing.tokens):
    idf_of_intersection = idf_all_tokens[token] + idf_of_intersection
  return ((idf_of_intersection / idf_of_name) -  (0.3 * (
            product.manufacturer not in listing.manufacturer and
              listing.manufacturer not in product.manufacturer)))


def tokenize_and_normalize(txt):
  token_set = tokenize(txt)
  token_set = filter_stop_words(token_set)
  return normalize(token_set)


def idf_of_all_tokens(products, listings):
  all_tokens = {}
  for product in products:
    for token in product.tokens:
      if token not in all_tokens:
        all_tokens[token] = 0
      all_tokens[token] = all_tokens[token] + 1
  for listing in listings:
    for token in listing.tokens:
      if token not in all_tokens:
        all_tokens[token] = 0
      all_tokens[token] = all_tokens[token] + 1
  idf_tokens = {}
  total = len(products) + len(listings)
  for token, doc_count in all_tokens.iteritems():
    idf_tokens[token] = (total * 1.0) / (doc_count + 1)
  return idf_tokens
