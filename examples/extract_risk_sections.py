import os
from pathlib import Path
from bs4 import BeautifulSoup
import re
from lxml.html.clean import clean_html
import lxml.html
import io
import html2text
import requests

part_pattern = re.compile("(?s)(?i)(?m)> +Part|>Part|^Part", re.IGNORECASE + re.MULTILINE)
item_pattern = re.compile("(?s)(?i)(?m)> +Item|>Item|^Item", re.IGNORECASE + re.MULTILINE)
substitute_html = re.compile("(?s)<.*?>")

# for example, I"m going to download filing directly
# set to the folderpath of an extracted 10-K filing
folderpath = r'C:\sec_gov\Archives\edgar\data\200406'
filename = r'0000200406-22-000022.txt'
filepath = os.path.join(folderpath, filename)

# read it into variable
with open(filepath, "r", encoding='utf-8') as f:
    raw_html = f.read()

# search for the parts/items of filing and replace it with unique character to split on later
updated_html = part_pattern.sub(">°Part", raw_html)
updated_html = item_pattern.sub(">°Item", updated_html)

# remove tables because they can be parsed seperately
lxml_html = lxml.html.fromstring(updated_html)
root = lxml_html.getroottree()

# remove tables because we can analyze them seperately
# table = list(root.iter(tag='table'))[11]
for i, table in enumerate(root.iter(tag='table')):

    table_text = table.text_content()

    # i just used two entries to determine whether we were looking at toc table
    if "Financial Data" in table_text or "Mine Safety Disclosures" in table_text:
        #print("Found Sections")
        #print(table_text)
        pass
    else:
        # drop table from HTML
        table.drop_tree()

updated_raw_html = lxml.html.tostring(root)

soup = BeautifulSoup(updated_raw_html, 'lxml')

h = html2text.HTML2Text()
raw_text = h.handle(soup.prettify())

combined_text = ""
file_count = 0

for idx, item in enumerate(raw_text.split("°Item")):
    if "risk factors" in item.lower():
        if len(item) > 100:
            first_line = item.splitlines()[0].strip()
            
            if "risk factors" in first_line.lower():
                file_count += 1
                combined_text += item

if file_count > 0:
    filename = f"risk_factors_{filename}"
    with io.open(os.path.join(folderpath, filename), "w", encoding='utf-8') as f:
        f.write(combined_text)
    

print(f"Risk Factor Sections Saved:\n{folderpath}")
