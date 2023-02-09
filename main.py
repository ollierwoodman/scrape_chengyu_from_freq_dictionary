from bs4 import BeautifulSoup as bs

SOURCE_FILE_PATH = 'source_test.html'
OUTPUT_FILE_PATH = '500_chengyu.json'

with open(SOURCE_FILE_PATH, 'r', encoding="utf-8") as f:
    source = f.read()

# clean up input data
substring_replacements = [
    ['\n',''],
    ['，',', '],
    ['’',"'"],
    ['‘',"'"],
]
for replacement in substring_replacements:
    source = source.replace(replacement[0], replacement[1])
    
# parse html
soup = bs(source, 'html.parser')

def isNodeAChengyuHeading(node):
    if node.name == 'h2':
        return True
    return False

children = soup.find_all(['h2','p'], recursive=False)

chengyu_list = []
chengyu = []
for child in children:
    if isNodeAChengyuHeading(child):
        chengyu_list.append(chengyu)
        chengyu = [child]
    else:
        chengyu.append(child)
        


print(chengyu_list)