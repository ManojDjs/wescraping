from pathlib import Path
import re
data_folder = Path("D://")
file_to_open = data_folder / "raw.txt"
f = open(file_to_open)
contents=f.read()
def cleanhtml(raw_html):
 cleanr = re.compile('<.*?[^/br]>')
 cleantext = re.sub(cleanr,'', raw_html)
 tags = re.compile(r'\n\n+')
 cleantext2 = re.sub(tags, r'<br/><br/>',cleantext)
 tags2 = re.compile(r'\n')
 cleantext3 = re.sub(tags2, r'<br/>',cleantext2)
 cleantext3.replace(r'\n','<br/>')
 return cleantext3
print(cleanhtml(contents))
