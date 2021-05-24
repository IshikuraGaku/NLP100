import re
import json

if __name__ ==  "__main__":
    #make_save_mappint()
    with open("neko_dic.json", "rt", encoding="utf-8") as f:
        analitics_list = json.load(f)
        print(type(analitics_list.values()))
        analitics_list = list(analitics_list.values())
        for i, dic in enumerate(analitics_list):
            if re.match("の", dic.get("base")):
                if re.match("名詞", analitics_list[i-1].get("pos")) and re.match("名詞", analitics_list[i+1].get("pos")):
                    out_txt = analitics_list[i-1].get("surface") + dic.get("surface") + analitics_list[i+1].get("surface")
                    print(out_txt)
                
