import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
from sklearn import svm

vectorizer = CountVectorizer(stop_words='english',ngram_range=(2,3))
fp = open('myfile','r')
tweets = fp.readlines()
fp1 = open('testFile','r')
tweets1 = fp1.readlines()
fp1 = open('stopwords.txt','r')
stopwrds = fp1.readlines()
#print(stopwrds)
'''my_list=[]
for one in stopwrds:
    one = one[:-1]
    one.lower()
    my_list.append(one)
'''
#--------------------------------------------------------------
Y=[int(r[0]) for r in tweets]                        #y values agayi
Y1 = [int(r[0]) for r in tweets1]                        #y test values agayi
'''
final_list =[]
for i in [r[1:] for r in tweets]:
    #print(i)
    wrd_list = i.split(' ')
    wrd_list = wrd_list[1:-1]
    new_list = []
    for wrd in wrd_list:
        if wrd.lower() not in my_list:
            new_list.append(wrd)
    string1 = " ".join(new_list)
    final_list.append(string1)

final_list1 =[]
for i in [r[1:] for r in tweets1]:
    #print(i)
    wrd_list = i.split(' ')
    wrd_list = wrd_list[1:-1]
    new_list = []
    for wrd in wrd_list:
        if wrd.lower() not in my_list:
            new_list.append(wrd)
    string1 = " ".join(new_list)
    final_list1.append(string1)
'''
#X= vectorizer.fit_transform(final_list)
X= vectorizer.fit_transform([r[1:] for r in tweets])
#X1= vectorizer.transform(final_list1)
X1= vectorizer.transform([r[1:] for r in tweets1])
#---------------------------------------------------------------------------------
model = svm.LinearSVC()
model.fit(X, Y)
#--------------------------------------------------------------
predictions = model.predict(X1)
print("Accuracy =", np.mean(predictions == Y1))
#------------------------------------------------------------
from sklearn import metrics
print(metrics.classification_report(Y1, predictions))
