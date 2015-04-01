from __future__ import print_function
from collections import Counter
from itertools import combinations, permutations, product
from operator import itemgetter
import os
import random
import string
import subprocess
import sys

def ex2():
    # an excerpt from sherlock holmes
    sentence_num = 3 # extract 'sentence_num' sentences from the book
    with open('holmes.txt', 'r') as doc:
        lines = doc.readlines()
    words_all = []
    dot_pos = []
    word_count = 0
    for line in lines:
        for word in line.split():
            if (word.endswith('.') or word.endswith('."')
                and not word.endswith('Mr.')):
                dot_pos.append(word_count)
            words_all.append(word)
            word_count += 1
    used_pos = random.randint(0, len(dot_pos) - sentence_num)
    start = dot_pos[used_pos]
    end = dot_pos[used_pos + sentence_num]
    text = ' '.join(words_all[start + 1: end + 1])
    return text

def ex1():
    # random numbers separated by random words
    print('ex10')
    lines = []
    words = words_list('holmes.txt', False)
    nums = [''.join(x) for x in product('12356', repeat=4)]
    for i in range(10):
        line = []
        for j in range(12):
            if j % 2 == 1:
                word = random.choice(nums)
            else:
                word = random.choice(words)
            line.append(word)
        lines.append(' '.join(line))
    text = '\n'.join(lines)
    return text

def words_list(filename, punc):
    if punc:
        exclude = ''
    else:
        exclude = string.punctuation
    with open(filename, 'r') as doc:
        lines = doc.readlines()
    words_all = []
    for line in lines:
        words_line = [w.strip(exclude) for w in line.split()]
        words_all += words_line
    c = Counter(words_all)
    common = c.most_common()
    least_common_tuples = sorted(common, key=itemgetter(1))[:7000]
    least_common = [t[0] for t in least_common_tuples if len(t[0]) > 5]
    return least_common

def main():
    if len(sys.argv) == 2:
        fn = 'ex{}()'.format(sys.argv[1])
        clipboard = eval(fn)
        with open('ex{}.txt'.format(sys.argv[1]), 'w') as doc:
            doc.write(clipboard)
    else:
        print('Usage: python ty.py 6')  # run ex6()

if __name__ == '__main__':
    main()
