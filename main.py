import argparse
from link import link

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--products_file', type=str, default='data/products.txt')
  parser.add_argument('--listings_file', type=str, default='data/listings.txt')
  parser.add_argument('--output_file', type=str, default='out.txt')
  return parser.parse_args()

if __name__ == '__main__':
  args = parse_args()
  link(args.products_file, args.listings_file, args.output_file)
