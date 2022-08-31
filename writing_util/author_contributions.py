#!/usr/bin/env python
'''
'''

import argparse
import collections
import csv
import logging
import sys

def list_with_and(l):
  if len(l) > 1:
    return '{} and {}'.format(', '.join(l[:-1]), l[-1])
  else:
    return l[0]

def main(fh_in, name, contributions, fh_out):
  authors_seen = set()
  conts = collections.defaultdict(set)
  for i, row in enumerate(csv.DictReader(fh_in)): # each author
    if i < 2:
      logging.debug(row)

    n = row[name].strip() # name of author

    if n == '':
      continue

    logging.debug('processing %s...', n)
    if n in authors_seen:
      logging.warn('%s is duplicated', n)
    authors_seen.add(n)

    contribution_count = 0
    for contribution in contributions: # contribution columns
      if row[contribution].strip() != '':
        conts[contribution].add(n)
        contribution_count += 1

    if contribution_count == 0:
      logging.warn('%s did not contribute...', n)

  # write all authors that contributed to each contribution
  for contribution in contributions:
    if len(conts[contribution]) == 0:
      logging.warn('Nobody contributed to %s', contribution)
      continue

    sys.stdout.write('{} contributed to {}.\n'.format(list_with_and(sorted(conts[contribution])), contribution))

  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate affiliations')
  parser.add_argument('--name', required=True, help='contributor name column')
  parser.add_argument('--contributions', nargs='+', required=True, help='affiliations fields')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(sys.stdin, args.name, args.contributions, sys.stdout)

