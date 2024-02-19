# read and process data just crawl on dagora

import os
import json

count_zodiac ={'rat':0,
               'ox':0,
               'dog':0,
               'cat':0,
               'dragon':0,
               'tiger':0,
               'snake':0,
               'goat':0,
               'horse':0,
               'monkey':0,
               'rooster':0,
               'pig':0}

def check_monkey(x):
    # if x['is_monkey']: 
    # if x['is_own']: 
    # if x['name'] == 'cat' and x['is_own']: 
    if x['name'] == 'dragon': 
        print(x)
        # count_zodiac[x['name']] += 1
        return 1
    return 0    

directory_path = 'C:\Sources\pyScript\dagora' # hard path
file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
count = 0

# Print the list of files
print(f'Files in directory "{directory_path}":')
for file in file_list:
    file_path = f'{directory_path}/{file}'
    with open(file_path, 'r') as file:
        data = json.load(file)
    a = list(map(check_monkey, data['data']))
    count += sum(a)
# print(count_zodiac)
print(count)