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

def main(fn, name, affiliations, title):

  document = Document()
  p = document.add_paragraph(title).bold = True

  logging.info('reading from %s...', fn)
  affs = {} # all affiliations
  affs_seen = set()
  next_aff = 1
  
  p = document.add_paragraph()

  for i, row in enumerate(csv.DictReader(open(fn, mode='r', encoding='utf-8-sig'))):
    if i < 2:
      logging.debug(row)

    if i > 0:
      p.add_run(', ').italic = True

    n = row[name] # name of author
    n_affs = set() # author affiliations
    for affiliation in affiliations:
      a = row[affiliation].strip()
      if a == '':
        continue
      n_affs.add(next_aff)

      if a not in affs_seen:
        affs[next_aff] = a
        next_aff += 1
        affs_seen.add(a)

    # write the author
    p.add_run(n).italic = True
    
    # author afiliations
    aff_txt = ','.join(sorted([str(x) for x in n_affs]))
    run = p.add_run(aff_txt)
    run.italic = True
    run.font.superscript = True

  # now write all the affs
  p = document.add_paragraph()

  for i in range(1, next_aff):
    if i > 1:
      p.add_run('; ').italic = True

    num = p.add_run(str(i))
    num.font.superscript = True
    num.italic = True

    text = affs[i]
    p.add_run(text).italic = True

  document.save('data.docx')

  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Assess MSI')
  parser.add_argument('--file', required=True, help='filename')
  parser.add_argument('--name', required=True, help='name field')
  parser.add_argument('--title', required=True, help='title')
  parser.add_argument('--affiliations', nargs='+', required=True, help='affiliations fields')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.file, args.name, args.affiliations, args.title)
