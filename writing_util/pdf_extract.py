#!/usr/bin/env python
'''
  extract individual pages of a pdf
  writes individual pages, since word only supports this
'''

import argparse
import logging
import sys

import PyPDF2    

def main(pdf, output):
  logging.info('starting...')
  pdf_reader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
  for n in range(pdf_reader.getNumPages()):
    start_page = n
    end_page = n
    target = output.format(n=n)
    logging.info('writing %s', target)
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(n))
    pdf_writer.write(open(target, 'wb'))

  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Print individual pages')
  parser.add_argument('--input', required=True, help='input pdf')
  parser.add_argument('--output', required=True, help='template of the form filename{n}.pdf')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.input, args.output)
