#!/usr/bin/env python
'''
  takes pdf files and make a new pdf with specified pages
'''

import argparse
import logging
import sys

import PyPDF2    

def main(pdfs, output):
  logging.info('opening %s for writing...', output)
  pdf_writer = PyPDF2.PdfFileWriter()
  for pdf in pdfs:
    filename, fromto = pdf.split(':')
    start, finish = [int(x) for x in fromto.split('-')]
    logging.info('reading from %s...', filename)
    pdf_reader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    for n in range(start, finish+1):
      logging.debug('adding page %i from %s...', n, filename)
      pdf_writer.addPage(pdf_reader.getPage(n-1))
      logging.debug('added page %i from %s', n, filename)

  logging.info('writing to %s...', output)
  pdf_writer.write(open(output, 'wb'))
  logging.info('writing to %s: done', output)

  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Print individual pages')
  parser.add_argument('--inputs', required=True, nargs='+', help='input pdfs of the form filename.pdf:from-to inclusive 1-based')
  parser.add_argument('--output', required=True, help='combined pdf')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.inputs, args.output)
