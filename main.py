from bs4 import BeautifulSoup as bs
import re
import json

SOURCE_FILE_PATH = 'source.html'
OUTPUT_FILE_PATH = '500_chengyu' # DO NOT INCLUDE .json FILE EXTENSION
OUTPUT_MINIFIED_FILE_PATH = OUTPUT_FILE_PATH + '_min' # DO NOT INCLUDE .json FILE EXTENSION

def isNodeAChengyuHeading(node):
    if node.name == 'h2':
        return True
    return False

def isString(var):
    if isinstance(var, str):
        return True
    return False

def exampleChineseSentenceNodetoString(node):
    out = ''
    for item in node.contents[1:]:
        if isString(item):
            out += item
        else:
            out += item.contents[0]
    return out.strip()

def saveVarToJsonFile(var, filename, pretty = False):
    if pretty:
        indent = 4
    else:
        indent = None
    
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(var, f, indent=indent, ensure_ascii=False)
        

with open(SOURCE_FILE_PATH, 'r', encoding="utf-8") as f:
    source = f.read()

# clean up input data
substring_replacements = [
    ['\n',''],
    ['’',"'"],
    ['‘',"'"],
    ['–',"-"],
    ['“','"'],
    ['”','"'],
    ['（','('],
    ['）',')'],
    ['【','['],
    ['】',']'],
]
for replacement in substring_replacements:
    source = source.replace(replacement[0], replacement[1])


soup = bs(source, 'html.parser')

children = soup.find_all(['h2','p'], recursive=False)

entry_list = list()
entry = []
for child in children:
    if isNodeAChengyuHeading(child):
        entry_list.append(entry)
        entry = [child]
    elif child == children[-1]:
        entry.append(child)
        entry_list.append(entry)
    else:
        entry.append(child)

entry_list.pop(0)

chengyu_list = {
    'entries': [],
    'citation': {
        'link': 'https://doi.org/10.4324/9780203839140',
        'apa': 'Jiao, L., Kubler, C. C., & Zhang, W. (2010). 500 Common Chinese Idioms: An annotated Frequency Dictionary. Routledge.',
    },
}

for entry in entry_list:
    current_entry = {}
    
    current_entry['phrase'] = {
        'zh-CN': re.search("\[(.+)\]", entry[0].a.contents[0]).group(1),
        'zh-HK': re.search("\((.+)\)", entry[0].a.contents[0]).group(1),
        'pinyin': re.search("\)\s*(.+)\Z", entry[0].a.contents[0]).group(1),
    }
    
    current_entry['translations'] = [
        {
            'english': entry[1].contents[0].string,
        },
    ]
    
    current_entry['examples'] = [
        {
            'simplified': exampleChineseSentenceNodetoString(entry[2]),
            'pinyin': entry[3].contents[0].string,
            'english': entry[4].contents[0].string,
        },
        {
            'simplified': exampleChineseSentenceNodetoString(entry[5]),
            'pinyin': entry[6].contents[0].string,
            'english': entry[7].contents[0].string,
        },
    ]
    
    chengyu_list['entries'].append(current_entry)

saveVarToJsonFile(chengyu_list, OUTPUT_FILE_PATH + '.json', True)
saveVarToJsonFile(chengyu_list, OUTPUT_MINIFIED_FILE_PATH + '.json')