# Chengyu scraping tool

This script was written to quickly scrape the Chengyu and their details from some html.   

## Description

Before writing the script, the Chengyu frequency dictionary [500 Common Chinese Idioms](https://doi.org/10.4324/9780203839140) was displayed using the Firefox ePub viewer [EPUBReader](http://www.epubread.com/). I copied the section of html containing all 500 Chengyu into an html file `source.html`, also creating an abbreviated version with 20 Chengyu for development and testing called `source_test.html`. From there I wrote the `main.py` script to extract as much of the data as possible and format it as an easily navigable `500_chengyu.json` JSON file.

## Getting Started

### Dependencies

[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Accessing the dataset

You can download the JSON file directly from the repo.

The copyright to the examples, definitions, etc. belong to the [original authors](https://doi.org/10.4324/9780203839140) and hence your usage of the dataset should be appropriately cited. The 500 chengyu themselves are not eligible for copyright and hence can be used without citation.

### Format of the JSON file

```
{
  "entries": [
    {
      "phrase": {
        "zhCN": "Simplified Chinese phrase",
        "zhHK": "Traditional Chinese phrase",
        "zhPY": "Pinyin transcription"
      },
      "translations": {
        "enGB": "Definition and explanation written in English"
      },
      "examples": [
        {
          "zhCN": "Example in simplified Chinese",
          "zhPY": "Pinyin transcription",
          "enGB": "English translation of example"
        },
        {
          "zhCN": "Another Example in simplified Chinese",
          "zhPY": "Pinyin Transcription",
          "enGB": "English translation of second example"
        }
      ]
    },
    ...
  ]  
  "citation": {
    "link": "Link to the source material's DOI permalink", 
    "apa": "Reference cited in APA format"
  }
}
```

### Installing

1. Install Beautiful Soup 4:
```
pip install beautifulsoup4
```
2. Clone the git repo or download the scripts

### Executing program

Edit the constants at the top of the `main.py` Python file and run the script
```
python ./main.py
```

## Known limitations

- Some notes refer to images that were not scraped

## Dataset source

Jiao, L., Kubler, C. C., & Zhang, W. (2010). 500 Common Chinese Idioms: An annotated Frequency Dictionary. Routledge. https://doi.org/10.4324/9780203839140