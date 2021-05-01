def make_char_bigram(input_sentence):
    char_bigram = [input_sentence[i:i+2] for i in range(len(input_sentence)-1)]
    
    return char_bigram

sentence1 = "paraparaparadise"
sentence2 = "paragraph"

#setで重複排除
set_bigram1 = set( make_char_bigram(sentence1) )
set_bigram2 = set( make_char_bigram(sentence2) )

#和集合　出てくる要素すべて
union_bigram = set_bigram1.union(set_bigram2)

#積集合　重なってる部分
intersection_bigram = set_bigram1.intersection(set_bigram2)

#差集合 1-2
difference_bigram = set_bigram1.difference(set_bigram2)

print(union_bigram)
print(intersection_bigram)
print(difference_bigram)
print(("se" in set_bigram1))
print(("se" in set_bigram2))
