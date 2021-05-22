import MeCab
import re

with open("neko.txt", "rb") as f:
    neko_txt = f.read()
    
    neko_txt = neko_txt.decode("utf-8")
    neko_txt = re.sub("\u3000", "", neko_txt)
    neko_sentence_list = neko_txt.split("\r\n")
    print(neko_sentence_list[0:10])
    analitics_list = []

    for line in neko_sentence_list:
        #タグ付け
        tagger = MeCab.Tagger()
        wakati_tag = tagger.parse(line)
        wakati_tag = re.sub(r"[0-9]", "", wakati_tag)
        wakati_tag = wakati_tag.split("\n")
        
        for i in wakati_tag:
            i = i.split()
            if len(i) < 4:
                continue
            dic = {}
            dic["surface"] = i[0]
            dic["base"] = i[3]   

            dic["pos"] = i[4]
            if len(wakati_tag) > 5:
                dic["pos1"] = " ".join(i[5:])
            else:
                dic["pos1"] = ""
            analitics_list.append(dic)
    print(analitics_list)
            

