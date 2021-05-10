f = open("popular-names.txt", "r")
#read　全部 readlines 一行ずつ

cf1 = open("col1.txt", "w") 
cf2 = open("col2.txt", "w")

ct1 = ""
ct2 = ""
rf = f.readlines()

for t in rf:
    t_list = t.split("\t")
    ct1 = ct1 + t_list[0] + "\n"
    ct2 = ct2 + t_list[1] + "\n"

cf1.write(ct1)
cf2.write(ct2)
