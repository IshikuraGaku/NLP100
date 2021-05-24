import re
import json

if __name__ ==  "__main__":
    #make_save_mappint()
    with open("neko_dic.json", "rt", encoding="utf-8") as f:
        analitics_list = json.load(f)
        print(type(analitics_list.values()))
        analitics_list = list(analitics_list.values())
        out_txt = ""
        count = 0
        for i in range(len(analitics_list)):
            if re.match("名詞", analitics_list[i].get("pos")):
                out_txt += analitics_list[i].get("surface")
                count += 1
            else:
                if out_txt != "" and count > 1:
                    print(out_txt)
                out_txt = ""
                count = 0
                
