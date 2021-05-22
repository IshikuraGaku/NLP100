import pandas as pd
import gzip
import re

#linesがないと開かない
df = pd.read_json("jawiki-country.json.gz", lines=True)

#^先頭　$ 末尾　これがないとstd=とかが引っかかる
#想定は \n==日本==\n
#r'^\[+ファイル:[^|]+\|'
#r'\{\{基礎情報(.+?)\n\}\}'
#もしかして改行移行のマッチングは出来ない？
pattern = r'\{\{基礎情報.+?\t\}\}'

dic_element={}
#lines = re.sub(r"\"|\'|\[|\]|\<|\>|#|\*|~|!", "", lines)



for title, lines in zip(df["title"], df["text"]):
    lines = re.sub("\n", "\t", lines)
    lines = re.sub(r"\<.+?\>", "", lines)
    lines = re.sub(r"\"|\'|\[|\]|#|\*|~|!", "", lines)
    
    line = re.findall(pattern, lines)
    
    #print(line)
    if len(line) == 0:
        continue

    line[0] = re.sub(r"\{+.+?\}+", "", line[0])
    for i in line[0].split("\t"):
        line_field = re.findall(r"\|(.+?)=", i)
        if len(line_field) == 0:
            continue
        
        line_field = re.sub(r"[ |\t]", "", line_field[0])
        #print(line_field)

        line_value = re.findall(r"=(.+?)$", i)
        if len(line_value) == 0:
            continue
        line_value = re.sub(r"[\t]", "", line_value[0])
        if line_value[0] == " ":
            line_value = line_value[1:]
        #print(line_value)

        dic_element[title+"_"+line_field] = line_value

import requests

for title in df["title"]:
    media_name = dic_element.get(title+"_"+"国旗画像")
    if media_name is None:
        continue
    media_name.replace
    if media_name is not None:
        print(media_name)
        url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + media_name + '&prop=imageinfo&iiprop=url&format=json'
        catched_data = requests.get(url)
        get_url = re.search(r'"url":"(.+?)"', catched_data.text)
        print(get_url.group(1))
