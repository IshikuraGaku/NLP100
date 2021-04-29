words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur, King Can."
words = words.replace(".", "").replace(",","")
print(words)
word = words.split(" ")

num=[1, 5, 6, 7, 8, 9, 15, 16, 19]

dic = {}
for i, w in enumerate(word):
    if i+1 in num:
        dic[w[0]] = i+1
    else:
        dic[w[0:2]] = i+1

print(dic)
