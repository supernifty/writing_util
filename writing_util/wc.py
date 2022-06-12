#!/usr/bin/env python

import sys

import docx

document = docx.Document(sys.argv[1])
text = '\n\n'.join(
    paragraph.text for paragraph in document.paragraphs
)
sys.stdout.write('{}\n'.format(len(text.split())))
