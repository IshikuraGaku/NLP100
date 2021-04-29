words = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = words.replace(",", "")
words = words.replace(".", "")
word = words.split()

num_of_word = []
for i in word:
     num_of_word.append(len(i))
print(num_of_word)
