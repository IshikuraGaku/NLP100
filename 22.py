import pandas as pd
import gzip

#linesがないと開かない
df = pd.read_json("jawiki-country.json.gz", lines=True)

#titleだけだと、dfの列情報もとる
#textを指定するとtextを取ってくるが、中身というより、要素を取るって感じ
#valuesだけだと改行とか綺麗にならない？
#values[0]にするといい感じ1はない
json_value = df["title"].values[:]
print(json_value)