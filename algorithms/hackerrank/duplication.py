with open('duplication.txt') as f:
        n = int(next(f).strip())

        s_initial = "0"
        s_expaneded = ""

        def opposite(word):
            word_out = ""
            for c in word:
                if c == "0":
                    word_out += "1"
                if c == "1":
                    word_out += "0"
            return word_out

        while len(s_expaneded) < 10000:
            t_initial = opposite(s_initial)
            s_expaneded = s_initial + t_initial
            s_initial = s_expaneded

        for i in range(n):
            x = int(next(f).strip())
            print s_expaneded[x]
