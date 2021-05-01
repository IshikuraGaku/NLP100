def make_char_bigram(input_sentence):
    char_bigram = [input_sentence[i:i+2] for i in range(len(input_sentence)-1)]
    
    return char_bigram

def make_word_bigram(input_sentence):
    input_words = [x.strip(" ,.?!") for x in input_sentence.split()]
    word_bigram = [input_words[i:i+2] for i in range(len(input_words)-1)] 
    
    return word_bigram

print("文字を入力してください")
input_sentence = input()

char_bigram = make_char_bigram(input_sentence)
word_bigram = make_word_bigram(input_sentence)

print(char_bigram)
print(word_bigram)

