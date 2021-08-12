
## Abbreviation Checker

### Make an abbreviations file
Of the form:
```
long name (short name)
```

### Generate a text version of your document
e.g. copy and paste to a text file

### Run the checker
```
python writing_util/abbreviations.py --abbreviations abbrev.txt < doc.txt | column -t -s'^I'
```
### Interpret
Check abbreviations with an "issue". 

### TODO
* currently the software doesn't check across lines

# Author Affiliations

authors.csv is a CSV file with author name and affiliations. Specify these on the command line to generate a word doc.

```
 python ../../../util/author_affiliations.py \
  --verbose \
  --input authors.csv \
  --output authors.csv \
  --name 'Full name' \
  --affiliations 'Affiliation 1' 'Affiliation 2' 'Affiliation 3' 'Affiliation 4' 'Affiliation 5' 'Affiliation 6' \
  --title 'Title of paper'
```
