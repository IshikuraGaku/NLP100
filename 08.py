import sys

def encode(input_sentence):
    
    encode_sentence = ""
    index_list = []
    for i, w in enumerate(input_sentence):
        if ord("a") <= ord(w) and ord(w) <= ord("z"):
            encode_sentence = encode_sentence + chr(219-ord(w))
            index_list.append(i)
        else:
            encode_sentence = encode_sentence + w

    return (index_list, encode_sentence)

def decode(index_list, encode_sentence):
    decode_sentence = ""
    for i, w in enumerate(encode_sentence):
        if i in index_list:
            decode_sentence = decode_sentence + chr(219-ord(w))
        else:
            decode_sentence += w
    
    return decode_sentence

input_sentence = "Grammar is very important 357 because It improves the quality of your writing!!"
index_list, encode_sentence = encode(input_sentence)
print(encode_sentence)

decode_sentence = decode(index_list, encode_sentence)
print(decode_sentence)


