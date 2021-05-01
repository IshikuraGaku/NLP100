import random

input_sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
input_sentence = input_sentence.strip(".:,")
input_sentence = input_sentence.split()

if 5 <= len(input_sentence):
    output_sentence = []
    output_sentence.append(input_sentence[0])
    output_sentence.extend(random.sample(input_sentence[1:len(input_sentence)-2],len(input_sentence[1:len(input_sentence)-2])))
    output_sentence.append(input_sentence[-1])
    output_sentence = " ".join(output_sentence)
else:
    output_sentence = " ".join(output_sentence)

print(output_sentence)