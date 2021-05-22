import pandas as pd
import gzip
import re

#linesがないと開かない
df = pd.read_json("jawiki-country.json.gz", lines=True)

#^先頭　$ 末尾　これがないとstd=とかが引っかかる
#想定は \n==日本==\n
#r'^\[+ファイル:[^|]+\|'
pattern = r'\[+ファイル:(.+?)\|'

for lines in df["text"]:
    for line in lines.split("\n"):
        #print(line)
        for i in re.findall(pattern, line):
            #i = re.sub(r"[+", "", i)
            print(i) 