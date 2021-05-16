import collections

class sort_class:
    def __init__(self):
        self.name_dir = {}
        
    def myfunc(self, e):
        #print(self.name_dir)
        #やっぱりカラムで渡せば複数いけるんだ！　天才かよ...
        return (int(self.name_dir.get(e[0], 0)), e[0], e[2])


    def sort_func(self):
        f = open("popular-names.txt", "r")

        char_list = f.readlines()
        char_list = [ w.split() for w in char_list]

        name_list = [w[0] for w in char_list]

        #ここでインスタンスメソッドに辞書を作成、重複がいくつあるかについて
        self.name_dir = collections.Counter(name_list)
        char_list.sort(reverse=True, key=self.myfunc)

        char_list_output = []
        for l in char_list:
            char_list_output.append(" ".join(l))
        char_list_output = "\n".join(char_list_output)

        return char_list_output

def main():
    sort_instance = sort_class()
    sorted_lines = sort_instance.sort_func()
    print(sorted_lines)

if __name__=="__main__":
    main()