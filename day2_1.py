import pandas as pd
import numpy as np


class Day2:

    def part_1(self):
        indiv_score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

        outcome = {'AX': 'D', 'AY': 'W', 'AZ': 'L',
                   'BX': 'L', 'BY': 'D', 'BZ': 'W',
                   'CX': 'W', 'CY': 'L', 'CZ': 'D'}

        result_score = {'L': 0, 'W': 6, 'D': 3}

        df = pd.read_csv('./data/day2_1.txt', delimiter=r"\s+", header=None)
        df.columns = ['elves', 'me']
        # print(df['elves'])
        df['combined'] = df['elves'] + df['me']
        df['my_score'] = 0
        sl = []
        for index, strg in df.iterrows():
            # print(strg['combined'])
            my_outcome = outcome[strg['combined']]
            my_result = result_score[my_outcome]
            # print(my_outcome, my_result,my_score)
            my_score = indiv_score[strg['me']]
            s = my_result + my_score
            sl.append(s)
            print(my_outcome, my_result, my_score, s)
        df['my_score'] = sl
        # print(df)
        df.to_csv('result.csv')
        total = df['my_score'].sum()
        print(total)
# A = ROCK 1, B= PAPER 2, C= SCISSOR 3
# X = 0, Y = 3, Z = 6
    def part_2(self):
        indiv_score = {'A': 1, 'B': 2, 'C': 3, 'X': 'L', 'Y': 'D', 'Z': 'W'}
        outcome = {'AX': 3, 'AY': 4, 'AZ': 8,
                   'BX': 1, 'BY': 5, 'BZ': 9,
                   'CX': 2, 'CY': 6, 'CZ': 7}

        df = pd.read_csv('./data/day2_1.txt', delimiter=r"\s+", header=0, usecols=['elves', 'me'])
        df['combined'] = df['elves'] + df['me']
        sl = []
        for index, strg in df.iterrows():
            # print(strg['combined'])
            s = outcome[strg['combined']]
            sl.append(s)
        df['my_score'] = sl
        total = df['my_score'].sum()
        print(total)