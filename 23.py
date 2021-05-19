import pandas as pd
import gzip
import re

#linesがないと開かない
df = pd.read_json("jawiki-country.json.gz", lines=True)

#titleだけだと、dfの列情報もとる
#textを指定するとtextを取ってくるが、中身というより、要素を取るって感じ
#valuesだけだと改行とか綺麗にならない？
#values[0]にするといい感じ1はない
#[0] str [:] np.darray??

#^先頭　$ 末尾　これがないとstd=とかが引っかかる
#想定は \n==日本==\n
pattern = r"^=+.*=+$"

for lines in df["text"]:
    for line in lines.split("\n"):
        for i in re.findall(pattern, line):
            num = i.count("=") // 2 - 1
            print(i,num) 
