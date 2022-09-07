#!/usr/bin/env python
'''
  given tumour and normal vcf pairs, explore msi status
'''

import argparse
import logging
import sys

import os
import fitz  # pip install --upgrade pip; pip install --upgrade pymupdf
from tqdm import tqdm # pip install tqdm

def main(pdf):
  logging.info('starting...')

  doc = fitz.Document(pdf)

  for i in tqdm(range(len(doc)), desc="pages"):
    for img in tqdm(doc.get_page_images(i), desc="page_images"):
      xref = img[0]
      image = doc.extract_image(xref)
      pix = fitz.Pixmap(doc, xref)
      out = "%s-p%s-%s.png" % (pdf[:-4], i, xref)
      logging.info('saving %s', out)
      pix.save(out)

  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Assess MSI')
  parser.add_argument('--pdf', required=True, help='tumour vcf')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.pdf)
