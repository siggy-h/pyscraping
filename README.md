# pyscraping
Html parsing with lxml and requests


# Usage 

For help context use ```./clean_02.py -h```

```bash
$ ./clean_02.py -h
usage: pyclean [-h] [-o OUTPUT_FILE] -t TAGS [TAGS ...] [-v] file

HTML Sanitizer.

positional arguments:
  file                  HTML input file to be cleansed.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        File to write output to.
  -t TAGS [TAGS ...], --tags TAGS [TAGS ...]
                        Tags to clean
  -v, --version         show program's version number and exit

```

```bash
./clean_02.py test00.html -t class style cellspacing data-mc-pattern -o out.txt
```

