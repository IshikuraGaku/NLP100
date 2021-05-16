def myfunc(e):

    return int(e[2])


f = open("popular-names.txt", "r")

char_list = f.readlines()
char_list = [ w.split() for w in char_list]
#print(char_list)
char_list.sort(reverse=True, key=myfunc)

char_list_output = []
for l in char_list:
    char_list_output.append(" ".join(l))
char_list_output = "\n".join(char_list_output)
print(char_list_output)