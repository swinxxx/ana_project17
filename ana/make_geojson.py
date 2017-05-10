import os, json
import pandas as pd
import string


def read_from_file():
    #mentioning path to file
    try:
        path1 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/cough.txt')
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

    # assigning geo data
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for one in data:
        for c in string.punctuation:
            single = one['text'].replace(c, "")
        tweet = single.lower()
        print('{} : {}'.format('coordinates', one['coordinates']))
        print("************")
        print("************")
        print("************")
        print("************")
        if(one['coordinates']):
            geo_json_feature = {
                "type": "Feature",
                "geometry": one['coordinates'],
                "properties": {
                    "text": tweet,
                    "created_at": ""
                }
            }
            geo_data['features'].append(geo_json_feature)

    # Save geo data
    with open('geo_data.json', 'w') as fout:
        fout.write(json.dumps(geo_data, indent=4))
read_from_file()