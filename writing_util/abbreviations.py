#!/usr/bin/env python
'''
  check abbreviations
'''

import argparse
import logging
import sys

def main(abbreviations):
  logging.info('starting...')
  abbrevs = {}
  for line in open(abbreviations, 'r'):
    fields = line.strip('\n)').split(' (')
    abbrevs[fields[0].lower()] = {'abbrev': fields[1], 'defined': [], 'long': [], 'short': []}
    #if fields[0].endswith('s') and fields[1].endswith('s'):
    #  abbrevs[fields[0][:-1].lower()] = {'abbrev': fields[1][:-1], 'defined': [], 'long': [], 'short': []}

  logging.info('reading from stdin')
  for idx, line in enumerate(sys.stdin):
    for lng in abbrevs.keys():
      # look for definition
      #if '{} ({})'.format(lng.lower(), abbrevs[lng]['abbrev'].lower()) in line.lower():
      if '{} ({}'.format(lng.lower(), abbrevs[lng]['abbrev'].lower()) in line.lower():
        abbrevs[lng]['defined'].append(idx)
        if len(abbrevs[lng]['defined']) > 1:
          logging.warn('%s defined again on line %i', lng, idx + 1)
      # look for long
      elif lng in line.lower():
        abbrevs[lng]['long'].append(idx)
        logging.warn('%s used should define or use abbreviation on line %i', lng, idx + 1)
      elif abbrevs[lng]['abbrev'] in line:
        abbrevs[lng]['short'].append(idx)
        if len(abbrevs[lng]['defined']) == 0:
          logging.warn('%s abbreviation used before definition on line %i', lng, idx + 1)

  sys.stdout.write('LongName\tShortName\tDefined\tLong\tShort\tIssue\n')
  for abbrev in abbrevs:
    issues = set()
    if len(abbrevs[abbrev]['defined']) == 0 and (len(abbrevs[abbrev]['long']) > 1 or len(abbrevs[abbrev]['short']) > 0):
      logging.warn('%s never defined', abbrev)
      issues.add('no_def')
    if len(abbrevs[abbrev]['defined']) > 1:
      logging.warn('%s defined multiple times', abbrev)
      issues.add('multiple_defs')
    if len(abbrevs[abbrev]['long']) > 1 or len(abbrevs[abbrev]['long']) > 0 and len(abbrevs[abbrev]['defined']) > 0:
      logging.warn('%s unabbreviated version used %i times', abbrev, len(abbrevs[abbrev]['long']))
      issues.add('long_version_used')
    if len(abbrevs[abbrev]['short']) == 0:
      logging.warn('%s abbreviation never used', abbrev)
      issues.add('abbrev_not_used')
    sys.stdout.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(abbrev, abbrevs[abbrev]['abbrev'], len(abbrevs[abbrev]['defined']), len(abbrevs[abbrev]['long']), len(abbrevs[abbrev]['short']), ','.join(issues)))
  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Check abbreviations')
  parser.add_argument('--abbreviations', required=True, help='file of abbreviations')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.abbreviations)
