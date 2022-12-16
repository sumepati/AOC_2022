# AoC Day 4
# Part 2 code has issue
class Day4_1:
    counta = 0
    countb = 0
    counter_1 =0
    counter_2 = 0
    count_no = 0
    count_no1 = 0
    def readfile(self) -> None:
        data = open('./data/day4_1.txt', 'r')
        content = data.readlines()
        for line in content:
            self.splitstring(line)
        print(self.counta + self.countb)

        print("part 2 ans",self.count_no )
    def splitstring(self,line):
        str = line
        str=str.split(',',2)
        #print(str)
        str_a=str[0].split('-')
        str_b = str[1].split('-')
        self.checkoverlap(str_a, str_b)
        self.checksubset(str_a,str_b)


    def checksubset(self,lst1,lst2):

        lst1 = lst1
        lst2 = lst2


        if int(lst1[0].strip()) >= int(lst2[0].strip()) and int(lst1[1].strip()) <= int(lst2[1].strip()):
            #print("Lst1 is subset of Lst2",lst1,lst2)
            self.counta += 1
            #print(self.count)
        elif int(lst2[0].strip()) >= int(lst1[0].strip()) and int(lst2[1].strip()) <= int(lst1[1].strip()):
            #print("Lst2 is subset of Lst1",lst1,lst2)
            self.countb += 1
            #print(self.count)
        else:
            #print("Lists do not overlap completely", lst1, lst2)
            cnt=0

    def checkoverlap(self,lst1,lst2):
        lst1 = lst1
        lst2 = lst2


        if int(lst1[1].strip()) < int(lst2[0].strip()) and int(lst1[1].strip()) < int(lst2[1].strip()):
            print("second element of first falls within second list ",lst1,lst2)
            self.count_no += 1
            # print(self.count) 15
            cnt =0
        #elif int(lst2[0].strip()) >= int(lst1[0].strip()) and int(lst2[1].strip()) <= int(lst1[1].strip()):
            #print("second list overlap with first", lst1, lst2)
            #self.count_no += 1
            #cnt = 0
        #elif int(lst1[0].strip()) == int(lst1[1].strip()) and int(lst1[0].strip()) == int(lst2[1].strip()):
            #print("first element = second element of first and second list overlap",lst1,lst2)
            #self.count_no += 1
            # print(self.count)
            #cnt = 0

        elif int(lst2[0].strip()) > int(lst1[0].strip()) and int(lst2[0].strip()) > int(lst1[1].strip()):
            print("first element of second list falls within first list", lst1, lst2)
            self.count_no += 1
            cnt = 0
        #else:
            #print("Lists do not overlap completely", lst1, lst2)

## aasthas97 reddit user
class copy:
    def redditlogic(self):

        import re

        with open('./data/day4_2.txt', 'r') as f:
            elvish_work = f.read().split("\n")

        part_one = 0
        part_two = 0
        for elf_pair in elvish_work:
            l1, l2, r1, r2 = [int(x) for x in re.split('[,-]', elf_pair)]
            print(l1,l2,r1,r2)
            elf1 = set(range(l1, l2 + 1))
            print(elf1)
            elf2 = set(range(r1, r2 + 1))
            print(elf2)
            if (elf1.issubset(elf2) or elf2.issubset(elf1)):
                part_one += 1
            if (elf1.intersection(elf2)):
                part_two += 1

        print("Part one:", part_one)
        print("Part two", part_two)