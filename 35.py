import re
import json

if __name__ ==  "__main__":
    #make_save_mappint()
    with open("neko_dic.json", "rt", encoding="utf-8") as f:
        analitics_list = json.load(f)
        print(type(analitics_list.values()))
        analitics_list = list(analitics_list.values())
        count_dic = {}
        for dic in analitics_list:
            if count_dic.get(dic.get("base")) is not None:
                count_dic[dic.get("base")] = count_dic[dic.get("base")] + 1
            else:
                count_dic[dic.get("base")] = 1
        count_dic = sorted(count_dic.items(), key=lambda x:x[1], reverse=True)
        print(count_dic)

                
                
