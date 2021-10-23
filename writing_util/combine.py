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

from docx import Document

def main(inputs, output):

  target = Document()

  for j, inp in enumerate(inputs):
    logging.info('opening %s', inp)

    if j == 0:
      target = Document(inp) # copy styles etc
    else:
      target.add_page_break()
      d = Document(inp)
      for element in d.element.body:
        target.element.body.append(element)

  logging.info('saving %s', output)
  target.save(output)
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

