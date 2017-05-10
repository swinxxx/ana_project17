import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
from sklearn import metrics


vectorizer = CountVectorizer(stop_words='english',ngram_range=(2,3))
fp = open('myfile','r')
tweets = fp.readlines()
fp1 = open('testFile','r')
tweets1 = fp1.readlines()
fp1 = open('stopwords.txt','r')
stopwrds = fp1.readlines()
#print(stopwrds)
my_list=[]
for one in stopwrds:
    one = one[:-1]
    one.lower()
    my_list.append(one)

test_target = [int(r[0]) for r in tweets]                        #y values agayi
test_target1 = [int(r[0]) for r in tweets1]                        #y test values agayi

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


train_features = vectorizer.fit_transform(final_list)
test_features = vectorizer.transform(final_list1)
clf = BernoulliNB()
clf.fit(train_features, [int(r[0]) for r in tweets])
# Now we can use the model to predict classifications for our test features.
predictions = clf.predict(test_features)


print("Accuracy =")
print(np.mean(predictions == test_target1))
print(metrics.classification_report(test_target1, predictions))



# Compute the error.  It is slightly different from our model because the internals of this process work differently from our implementation.
#fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
#print("Multinomial naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))
