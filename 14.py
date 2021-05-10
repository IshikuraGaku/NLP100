f = open("popular-names.txt", "r")
input_num = input("Enter number of lines\n")

for i in range(int(input_num)):
    print(f.readline(),end="")