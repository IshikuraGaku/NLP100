import MeCab
import re
import json

if __name__ ==  "__main__":
    #make_save_mappint()
    with open("neko_dic.json", "rt", encoding="utf-8") as f:
        analitics_list = json.load(f)
        for dic in analitics_list.values():
            #print(dic)
            if re.match("動詞", dic.get("pos")) and not re.match("助動詞", dic.get("pos")) and not  re.match("形容動詞", dic.get("pos")):
                print(dic.get("surface"))