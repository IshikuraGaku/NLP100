f = open("popular-names.txt", "r")
input_num = input("Enter number of lines\n")
text_list = f.readlines()
text_len = len(text_list)

for i in range(int(input_num)):
    print(text_list[text_len -int(input_num) + i], end="")
   