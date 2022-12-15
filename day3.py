# AoC Day 3

class Day3:
    lower_alpha = {'a': 1,
                   'b': 2,
                   'c': 3,
                   'd': 4,
                   'e': 5,
                   'f': 6,
                   'g': 7,
                   'h': 8,
                   'i': 9,
                   'j': 10,
                   'k': 11,
                   'l': 12,
                   'm': 13,
                   'n': 14,
                   'o': 15,
                   'p': 16,
                   'q': 17,
                   'r': 18,
                   's': 19,
                   't': 20,
                   'u': 21,
                   'v': 22,
                   'w': 23,
                   'x': 24,
                   'y': 25,
                   'z': 26
                   }
    upper_alpha = {'A': 27,
                   'B': 28,
                   'C': 29,
                   'D': 30,
                   'E': 31,
                   'F': 32,
                   'G': 33,
                   'H': 34,
                   'I': 35,
                   'J': 36,
                   'K': 37,
                   'L': 38,
                   'M': 39,
                   'N': 40,
                   'O': 41,
                   'P': 42,
                   'Q': 43,
                   'R': 44,
                   'S': 45,
                   'T': 46,
                   'U': 47,
                   'V': 48,
                   'W': 49,
                   'X': 50,
                   'Y': 51,
                   'Z': 52
                   }

    def readfile(self) -> None:
        data = open('./data/day3_1.txt', 'r')
        content = data.readlines()

        for line in content:
            print(line)
            self.split_halfway(line)
        #print("Hi", self.lst_upper, self.lst_lower)
        sm = sum(self.lst_upper) + sum(self.lst_lower)
        print("Sum", sm)
    def split_halfway(self, string) -> str:
        s1 = string[:int(len(string) / 2)]
        s2 = string[int(len(string) / 2):]
        #print(s1, s2)
        self.loop_logic(s1, s2)

    lst_lower = []
    lst_upper = []

    def loop_logic(self, s1, s2):
        s2.strip()

        lst_lower_tmp = []
        lst_upper_tmp = []
        scr_lower = []
        scr_upper = []
        for k1, v1 in enumerate(s1):
            # print(i)
            for k2, v2 in enumerate(s2):
                if v1 == v2:
                    if v1.isupper():
                        score_upper = self.upper_alpha[v1]
                        #print("IF " + v1, score_upper)
                        lst_upper_tmp.append(score_upper)

                        break
                    else:
                        score_lower = self.lower_alpha[v1]
                        #print("else " + v1, score_lower)
                        lst_lower_tmp.append(score_lower)

                        break
        #print(lst_upper_tmp,lst_lower_tmp)
        if len(lst_upper_tmp) !=0 :
            self.lst_upper.append(lst_upper_tmp[0])
        if len(lst_lower_tmp) !=0 :
            self.lst_lower.append(lst_lower_tmp[0])

class Day3_2:
    final_list = []
    final_score = []
    def readfile_2(self) -> None:
        n=3
        with open('./data/day3_1.txt', 'r') as infile:
            lines = []
            for line in infile:
                lines.append(line.strip())
                if len(lines) >= n:
                    print("Inside FOR",lines)
                    self.setlogic(lines)
                    lines = []
            if len(lines) > 0:
                print("Inside last IF",lines)

        print(self.final_list)
        self.calculate_score(self.final_list)
        print(sum(self.final_score))


    def setlogic(self,lines) -> None:
            s1=set(lines[0])
            s2=set(lines[1])
            s3=set(lines[2])
            common = s1 & s2 & s3
            #print("Common is ",common,type(common))
            for i in common :
                self.final_list.append(i)

    def calculate_score(self,fnl_list):

        fnl_list = self.final_list

        for i in fnl_list:
            #print(i)
            if i.islower():
                scr_lower = Day3.lower_alpha[i]
                self.final_score.append(scr_lower)
                #print(scr_lower)
            else:
                scr_upper = Day3.upper_alpha[i]
                self.final_score.append(scr_upper)
                #print(scr_upper)