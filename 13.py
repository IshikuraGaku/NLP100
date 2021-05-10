f = open("popular-names.txt", "r")
#read　全部 readlines 一行ずつ
rf = f.readlines()

a = ""

for t in rf:
    t_list = t.split("\t")
    a = a + t_list[0] + "\t" + t_list[1] + "\n"


print(a)