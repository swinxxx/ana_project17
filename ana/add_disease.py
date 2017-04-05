import random
import os
import re
import pandas as pd


def fun():
    try:
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/positive.csv')
        path1 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/all.csv')
    except:
        print('error')
    csv_input = pd.read_csv(path)
    csv_input['disease']='flu'
    csv_input['place']='florida'
    for index, row in csv_input.iterrows():
        if re.search('vaccine', row[0], re.IGNORECASE) != None :
            row[2]='vaccine'
        if re.search('cough', row[0], re.IGNORECASE) != None :
            row[2] = 'cough'

    #-----------------------------------------------------------------------------------------------------------------------------------------

    all_input = pd.read_csv(path1)
    li=[]
    li=all_input['place']

    for index, row in csv_input.iterrows():
        flag=0
        for ind, rowi in all_input.iterrows():
            if(str(row[0])==str(rowi[2])):
                row[3] = rowi[1]
                flag=1
                break
        if flag == 0 :
            row[3] = random.choice(li)


#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------neutral----------------------------------------------------------------------------------

    try:
        path_neu = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/neutral.csv')
    except:
        print('error')
    csv_neu = pd.read_csv(path_neu)
    csv_neu['disease']='flu'
    csv_neu['place']='florida'
    for index, row in csv_neu.iterrows():
        if re.search('vaccine', row[0], re.IGNORECASE) != None :
            row[2]='vaccine'
        if re.search('cough', row[0], re.IGNORECASE) != None :
            row[2] = 'cough'

    #-----------------------------------------------------------------------------------------------------------------------------------------

    for index, row in csv_neu.iterrows():
        flag=0
        for ind, rowi in all_input.iterrows():
            if(str(row[0])==str(rowi[2])):
                flag=1
                row[3] = rowi[1]
                break
            if flag == 0:
                row[3] = random.choice(li)




#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------negative----------------------------------------------------------------------------------

    try:
        path_neg = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/negative.csv')
    except:
        print('error')
    csv_neg = pd.read_csv(path_neg, encoding = "ISO-8859-1")
    csv_neg['disease']='flu'
    csv_neg['place']='florida'

    for index, row in csv_neg.iterrows():
        if re.search('vaccine', row[0], re.IGNORECASE) != None :
            row[2]='vaccine'
        if re.search('cough', row[0], re.IGNORECASE) != None :
            #print("{} \t {}".format(str(row[0]), 'cough'))
            row[2] = 'cough'

    #-----------------------------------------------------------------------------------------------------------------------------------------

    all_input.values.T.tolist()
    for index, row in csv_neg.iterrows():
        flag=0
        for ind, rowi in all_input.iterrows():
            if(str(row[0])==str(rowi[2])):
                flag=1
                row[3] = rowi[1]
                break
        if flag == 0 :
            row[3] = random.choice(li)
    print(csv_input)
    print("*****************************************************")
    print(csv_neg)
    print("*****************************************************")
    print(csv_neu)
    print("*****************************************************")




#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------writing to file----------------------------------------------------------------------------------

    try:
        path_out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/final_file.csv')
    except:
        print('error')

    with open(path_out, 'a') as out:
        csv_input.to_csv(out)
        csv_neg.to_csv(out)
        csv_neu.to_csv(out)

fun()
