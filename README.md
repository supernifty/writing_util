
## How to use

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

## TODO
* currently the software doesn't check across lines
