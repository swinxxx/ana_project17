import numpy as np
import os, re, string, operator
import pandas as pd
import matplotlib.pyplot as plt
import random


def TermBased():
    try:
        path1 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/all.csv')
    except:
        print('error')
    csv_input = pd.read_csv(path1)
    tweet = csv_input['tweet']
    frequency_track = {}
    for single in tweet:
        #remove urls
        single = re.sub(r"http\S+", "",single, flags=re.MULTILINE)

        #removing punctuations
        for c in string.punctuation:
            single = single.replace(c, "")

        #breaking lines into words ka array
        words = single.split()

        #calculating frequency
        for word in words:
            if word in frequency_track:
                frequency_track[word] += 1
            else:
                frequency_track[word] = 1

    # number of chunks

    ran_num1 = random.randint(1,len(frequency_track))
    print(ran_num1)
    i=0
    while i < ran_num1:
        ran_num2 = random.randint(1, int(len(frequency_track) / 50))                 #unequal probabilities
        print(ran_num2)
        j=ran_num2
        #while j > (ran_num2+49) :

TermBased()
