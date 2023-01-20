import json

file_path = '/home/testdata/All_Beauty_5.json'

json_data = []
with open(file_path, 'r') as f:
    for line in f:
        json_data.append(json.loads(line))
user = []
item = []
for i in json_data:
    user.append(i['reviewerID'])
    item.append(i['asin'])
for i in range(len(user)):
    print(user[i], item[i])
