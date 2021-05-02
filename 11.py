f = open("popular-names.txt", "r")
#read　全部 readlines 一行ずつ
text_file = f.read()

text_file = text_file.replace("\t"," ")
#\tはtab
print(text_file)