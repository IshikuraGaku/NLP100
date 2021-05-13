f = open("popular-names.txt", "r")

char_list = f.readlines()
char_list = [ w.split()[0] for w in char_list]

char_set = set(char_list)

print(char_set)











