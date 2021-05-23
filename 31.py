import MeCab
import re
import json

def make_save_mappint():
    with open("neko.txt", "rb") as f:
        neko_txt = f.read()
        
        neko_txt = neko_txt.decode("utf-8")
        neko_txt = re.sub("\u3000", "", neko_txt)
        neko_sentence_list = neko_txt.split("\r\n")
        #print(neko_sentence_list[0:10])
        analitics_dic = {}

        for i, line in enumerate(neko_sentence_list):
            #タグ付け
            tagger = MeCab.Tagger()
            wakati_tag = tagger.parse(line)
            wakati_tag = re.sub(r"[0-9]", "", wakati_tag)
            wakati_tag = wakati_tag.split("\n")
            
            for j, w in enumerate(wakati_tag):
                w = w.split()
                if len(w) < 4:
                    continue
                dic = {}
                dic["surface"] = w[0]
                dic["base"] = w[3]   

                dic["pos"] = w[4]
                if len(wakati_tag) > 5:
                    dic["pos1"] = " ".join(w[5:])
                else:
                    dic["pos1"] = ""
            
                analitics_dic[str(i)+str(j)] = dic
        
        with open("neko_dic.json", "wt", encoding="utf-8") as out_f:
            json.dump(analitics_dic, out_f, ensure_ascii=False, indent=2)
    
    return None


if __name__ ==  "__main__":
    #make_save_mappint()
    with open("neko_dic.json", "rt", encoding="utf-8") as f:
        analitics_list = json.load(f)
        for dic in analitics_list.values():
            #print(dic)
            if re.match("動詞", dic.get("pos")) and not re.match("助動詞", dic.get("pos")) and not  re.match("形容動詞", dic.get("pos")):
                print(dic.get("base"))