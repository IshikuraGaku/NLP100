word_odd = "パタトクカシーー"
print(word_odd[::2]+word_odd[1::2])
word_P = word_odd[::2]
word_T = word_odd[1::2]
word = ""
for i in range(4):
    word = word + word_P[i] + word_T[i] 
print(word)
