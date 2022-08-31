#!/usr/bin/env python
'''
  word doc of author list from spreadsheet

  installation:
    pip install python-docx
'''

import argparse
import csv
import logging
import sys

#from docx import Document

from docxcompose.composer import Composer
from docx import Document

def main(inputs, output):
  for j, inp in enumerate(inputs):
    logging.info('adding %s', inp)
    if j == 0:
      target = Document(inp)
      composer = Composer(target)
    else:
      sub = Document(inp)
      composer.append(sub)
  logging.info('saving %s', output)
  composer.save(output)
  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate affiliations')
  parser.add_argument('--inputs', required=True, nargs='+', help='input word docs')
  parser.add_argument('--output', required=False, default='data.docx', help='output word doc')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.inputs, args.output)

