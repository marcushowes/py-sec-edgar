import os
from pathlib import Path
from bs4 import BeautifulSoup
import re
from lxml.html.clean import clean_html
import lxml.html
import io
import html2text
import iterating_two_files
import making_excel


def read_file_in_chunks(filepath, chunk_size=1*1024*1024, max_size=10*1024*1024):
    with open(filepath, "r", encoding='utf-8') as f:
        raw_html = ""
        chunk = f.read(chunk_size)
        while chunk and len(raw_html) + len(chunk) <= max_size:
            raw_html += chunk
            chunk = f.read(chunk_size)
    return raw_html

part_pattern = re.compile("(?s)(?i)(?m)> +Part|>Part|^Part", re.IGNORECASE + re.MULTILINE)
item_pattern = re.compile("(?s)(?i)(?m)> +Item|>Item|^Item", re.IGNORECASE + re.MULTILINE)
substitute_html = re.compile("(?s)<.*?>")

# for example, I"m going to download filing directly
# set to the folderpath of an extracted 10-K filing
folderpath = r'C:\sec_gov\Archives\edgar\data'

# ---------------- FILE ITERATION AND RISK FACTOR SCRAPE ----------------

for root, dirs, files in os.walk(folderpath):
    for filename in files:
        filepath = os.path.join(root, filename)

        if os.path.isfile(filepath):

            raw_html = read_file_in_chunks(filepath)

            # search for the parts/items of filing and replace it with unique character to split on later
            updated_html = part_pattern.sub(">°Part", raw_html)
            updated_html = item_pattern.sub(">°Item", updated_html)

            # remove tables because they can be parsed seperately
            lxml_html = lxml.html.fromstring(updated_html)
            base = lxml_html.getroottree()

            # remove tables because we can analyze them seperately
            # table = list(root.iter(tag='table'))[11]
            for i, table in enumerate(base.iter(tag='table')):

                table_text = table.text_content()

                # i just used two entries to determine whether we were looking at toc table
                if "Financial Data" in table_text or "Mine Safety Disclosures" in table_text:
                    pass
                else:
                    # drop table from HTML
                    table.drop_tree()

            updated_raw_html = lxml.html.tostring(base)
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
                with io.open(os.path.join(root, filename), "w", encoding='utf-8') as f:
                    f.write(combined_text)
                

            print(f"Risk Factors Sections Saved:\n{folderpath}, {filename}")


# ---------------- COMPARE SIMILARITY INTO EXCEL ----------------

making_excel.create_excel(folderpath)

for root, dirs, files in os.walk(folderpath):
    for dirname in dirs:
        
        # Do something with each subdirectory
        subdir_path = os.path.join(root, dirname)

        # Call the function to process the files that come a year after the other
        iterating_two_files.process_files(folderpath, subdir_path)

print(f"\n DONE! \n")