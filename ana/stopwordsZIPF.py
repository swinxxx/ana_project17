import os, re, string, operator
import pandas as pd


def read_tweets():
    try:
        path1 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/all.csv')
        path2 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/stopwords.txt')
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

    #sorted by frequency, returns list
    sorted_frequency = sorted(frequency_track.items(), key=operator.itemgetter(1))

    #calculating a threshold frequency (2% of total occuring words), to be removed from the top an bottom
    sum = 0
    for element in sorted_frequency:
        sum += element[1]
    threshold = int(0.02 * sum)
    print(len(sorted_frequency))

    #removing singletons (words with frequency 1) and words above the upper threshold and lower threshold (2% of sum)
    stopwords=[]
    less=0
    more=sum
    for element in sorted_frequency:
        if element[1] == 1 :
            stopwords.append(element)
        elif less < threshold:
            less += element[1]
            stopwords.append(element)
        elif more > (sum-threshold):
            more -= element[1]
            stopwords.append(element)
    for element in stopwords:
        sorted_frequency.remove(element)
    with open(path2, 'a') as f:
        for key, value in stopwords:
            print(key)
            f.write(key)
            f.write('\n')


#STOPWORDS me dynamically calculated, stopwords agaye, based on zipfs law
#TODO:::::::::::::disease names chale jaege top frequency words me, unko hatana hai---------------------> do later!!!!!!!!!!!!!

read_tweets()









#how to generate stoplist for the new tweet???????????????????????????????????????