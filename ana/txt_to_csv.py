import os, json
import pandas as pd
import string


def read_from_file():
    #mentioning path to file
    try:
        path1 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/dengue.txt')
    except:
        print('error')

    #opening file
    file = open(path1, 'r')

    #reading from file
    from_file = file.read()

    #to remove extra comma at the end
    from_file = from_file[:-1]
    # adding square brackets to make a list format
    from_file = '[' + from_file + ']'

    #from string to list of jsons
    data = json.loads(from_file)

    #making a dataframe of the required value sets
    dictionary_array = []
    print(data[0])
    for xyz in data:
        flag=0
        temp_dict = {}
        for c in string.punctuation:
            single = xyz['text'].replace(c, "")
        temp_dict['tweet'] = single.lower()
        temp_dict['tweet'] = temp_dict['tweet'].replace('\n', ' ')
        #temp_dict['tweet'] = temp_dict['tweet'].replace('&amp;', ' and ')
        #temp_dict['tweet'] = temp_dict['tweet'].replace('&lt', ' less than ')
        #temp_dict['tweet'] = temp_dict['tweet'].replace('&gt', ' greater than ')
        temp_dict['tweet'] = temp_dict['tweet'].replace('\t', ' ')
        if xyz['user']:
            temp_dict['user_id'] = xyz['user']['id']
            temp_dict['user_location'] = xyz['user']['location']
            temp_dict['user_name'] = xyz['user']['name']
            temp_dict['user_handle'] = xyz['user']['screen_name']
        if xyz['coordinates']:
            temp_dict['coordinates'] = xyz['coordinates']['coordinates']
        '''else:
            temp_dict['coordinates'] = 'none'''''
        if xyz['geo']:
            temp_dict['geo'] = xyz['geo']['coordinates']
        '''else:
            temp_dict['geo'] = 'none'''''
        temp_dict['created_at'] = xyz['created_at']
        # use in case need to remove re-tweeted data
        '''try:
            print(xyz['retweeted_status'])
        except:
            print("none")'''
        if xyz['place']:
            temp_dict['place_name'] = xyz['place']['full_name']
            temp_dict['country'] = xyz['place']['country']
            temp_dict['place_id'] = xyz['place']['id']
        '''else:
            temp_dict['place_name'] = 'none'
            temp_dict['country'] = 'none'
            temp_dict['place_id'] = 'none'''''
        temp_dict['disease'] = 'Dengue'
        temp_dict['nature'] = 'NA'
        #if "dengue" in temp_dict['tweet'] or "malaria" in temp_dict['tweet'] or "cough" in temp_dict['tweet']:
        #    dictionary_array.append(temp_dict)
        dictionary_array.append(temp_dict)
    df= pd.DataFrame(dictionary_array)

    try:
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/alltweets.csv')
    except:
        print('error')
    with open(path, 'a') as out:
        df.to_csv(out)

read_from_file()




# HELP FOR LATER: To read only some columns from file!
'''
import os
import pandas as pd


def read_from_file():
    #mentioning path to file
    try:
        path1 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/alltweets.csv')
    except:
        print('error')
    fields = ['place_id', 'tweet']   -> mention column names!!
    df = pd.read_csv('alltweets.csv', skipinitialspace=True, usecols=fields)
    print(df)
    # See the keys
    #print (df.keys())
    # See content in 'star_name'
    #print (df.nature)

read_from_file()
'''