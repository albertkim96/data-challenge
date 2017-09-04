# Shopify Data Engineering Challenge - Mokai (Monica) Xu

import json
from pprint import pprint


def get_file(file):
    """Returns JSON file as Python dictionary"""
    with open(file) as data_file:
        return json.load(data_file)


def sort_data(data, field):
    """Sorts JSON Array by value of object's field"""
    return sorted(data, key=lambda x: x[field])


def inner_join(sorted_1, sorted_2, key1, key2):
    """Return inner join of two JSON Arrays sorted by respective key, given that sorted_1 key1 are all unique"""
    p1 = 0
    p2 = 0
    result = []

    while (p1 < len(sorted_1) and p2 < len(sorted_2)):
        # if entries
        if sorted_1[p1][key1] == sorted_2[p2][key2]:
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


def calc_total(records, names):
    """Return total price paid by customers with names indicated in names array """
    total = 0
    for rec in records:
        if rec['name'] in names:
            total += rec['price']
    return total

# sort both JSON Arrays, increment pointers, add to new inner join dictionary


def main(file1, file2, key1, key2):
    data1 = get_file(file1)
    data2 = get_file(file2)
    sorted_1 = sort_data(data1, key1)
    sorted_2 = sort_data(data2, key2)

    result = inner_join(sorted_1, sorted_2, key1, key2)
    pprint(calc_total(result, ['Barry', 'Steve']))  # The total is 19.5
    pprint(len(result))  # The length is 6
    return result


main('data/customers.json', 'data/orders.json', 'cid', 'customer_id')
