f = open("popular-names.txt", "r")
split_num = input("Enter number of split\n")


text_list = f.readlines()
text_len = len(text_list)


part_line_num = text_len // int(split_num)
part_line_mod = text_len % int(split_num)

print(part_line_num)

prev = 0
next = 0
a_list = []
for i in range(int(split_num)):
    print("part"+str(i+1))
    if(i+1 <= part_line_mod):
        next = prev + part_line_num+1    
    else:
        next = prev + part_line_num

    print(str(prev) + "to"+ str(next))
    a_list.append("".join(text_list[prev:next]))
    prev = next
    
print(a_list[2])



