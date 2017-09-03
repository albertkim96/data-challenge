import json
from jsonmerge import merge, Merger
from pprint import pprint


with open('data/orders.json') as data_file:    
    orders = json.load(data_file)

with open('data/customers.json') as data_file:
    customers = json.load(data_file)



###
schema = {
    "properties": {
        "bar": {
            "mergeStrategy": "append"
        }
    }
}

merger = Merger(schema)
'''
# convert both to dictionaries where the key is "cid and  "customer_id"
## helper function that will output array of key-value fields where cid is not one of them

# for each customer in customers
# if customer[cid] exists in orders DICTIONARY
# add get(customer[cid]) orderObject and add it to the json u are on
order_dict = {}
for order in orders:
    order_dict[order['customer_id']] = order

for customer in customers:
    if customer['cid'] in order_dict:
        result = merger.merge(customer, order_dict.get(customer['cid']))
        print(result)


customer_dict = {}
for customer in customers:
    customer_dict[customer['cid']] = customer
    
arr = []

for order in orders:
    if order['customer_id'] in customer_dict:
        result = merger.merge(order, customer_dict.get(order['customer_id']))
        arr.append(result)

print(arr)'''

#Build a simple joiner that accepts two files each containing an array of json objects. The user can specify any key that is shared in both files to join on. 

def main(file1, file2, key1, key2):
    with open(file1) as data_file:    
        dict1 = json.load(data_file)

    with open(file2) as data_file:
        dict2 = json.load(data_file)
    
    new_dict = {}
    for i in range(len(dict1)):
        new_dict[dict1[i][key1]] = dict1[i]
    
    res = []
    for i in range(len(dict2)):
        if dict2[i][key2] in new_dict:
            dict2[i].update(new_dict.get(dict2[i][key2]))
            res.append(dict2[i])

    print(res)


        
main('data/orders.json', 'data/customers.json', 'customer_id', 'cid')
        

        