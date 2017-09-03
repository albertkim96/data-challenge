import json
import operator
from jsonmerge import merge, Merger
from pprint import pprint


with open('data/orders.json') as data_file:    
    orders = json.load(data_file)

with open('data/customers.json') as data_file:
    customers = json.load(data_file)


sorted_orders = sorted(orders, key=lambda x: x['customer_id'])
#pprint(sorted_orders)
sorted_customers = sorted(customers, key=lambda x: x['cid'])
#pprint(sorted_customers)

result = []
p_customer = 0
p_order = 0

while (p_customer < len(sorted_customers) and p_order < len(sorted_orders)):
    if sorted_customers[p_customer]['cid'] == sorted_orders[p_order]['customer_id']:
        #add both things to new empty object
        entry = {}
        entry.update(sorted_customers[p_customer])
        entry.update(sorted_orders[p_order])
        result.append(entry)
        p_order = p_order + 1
    elif sorted_customers[p_customer]['cid'] < sorted_orders[p_order]['customer_id']:
        p_customer = p_customer + 1
    elif sorted_customers[p_customer]['cid'] > sorted_orders[p_order]['customer_id']:
        p_order = p_order + 1

#pprint(result)

def get_file(file):
    with open(file) as data_file:
        return json.load(data_file)
        
    
def sort_data(data, key_func):
    return sorted(data, key=lambda x: x[key_func])

def inner_join(sorted_1, sorted_2, key1, key2):
    p1 = 0
    p2 = 0
    result = []

    while (p1 < len(sorted_1) and p2 < len(sorted_2)):
        if sorted_1[p1][key1] == sorted_2[p2][key2]:
            #add both things to new empty object
            entry = {}
            entry.update(sorted_1[p1])
            entry.update(sorted_2[p2])
            result.append(entry)
            p2 = p2 + 1
        elif sorted_1[p1][key1] < sorted_2[p2][key2]:
            p1 = p1 + 1
        elif sorted_1[p1][key1] > sorted_2[p2][key2]:
            p2 = p2 + 1
    return result
def calc_total(records):
    total = 0
    for rec in records:
        if rec['name'] == 'Barry' or rec['name'] == 'Steve':
            total += rec['price']
    return total

# file1 has the unique ones
def main(file1, file2, key1, key2):
    data1 = get_file(file1)
    data2 = get_file(file2)
    sorted_1 = sort_data(data1, key1)
    sorted_2 = sort_data(data2, key2)
    
    result = inner_join(sorted_1, sorted_2, key1, key2)
    pprint(calc_total(result))
    pprint(len(result))
    return result
    

    #length of resulting array and the total spent between  Bry and steve

main('data/customers.json', 'data/orders.json', 'cid', 'customer_id')


