# Shopify Data Engineering Challenge - Mokai (Monica) Xu

import json
from pprint import pprint


def get_file(file):
    """Returns JSON file as Python dictionary"""
    with open(file) as data_file:
        return json.load(data_file)


def inner_join(sorted1, sorted2, key1, key2):
    """Return inner join of two JSON Arrays sorted by respective key, given that sorted_1 key1 are all unique"""
    p1 = 0
    p2 = 0
    result = []

    while (p1 < len(sorted1) and p2 < len(sorted2)):
        # if entries
        if sorted1[p1][key1] == sorted2[p2][key2]:
            entry = {}
            entry.update(sorted1[p1])
            entry.update(sorted2[p2])
            result.append(entry)
            p2 = p2 + 1
        elif sorted1[p1][key1] < sorted2[p2][key2]:
            p1 = p1 + 1
        elif sorted1[p1][key1] > sorted2[p2][key2]:
            p2 = p2 + 1
    return result


def calc_total(records, names):
    """Return total price paid by customers with names indicated in names array """
    total = 0
    for rec in records:
        if rec['name'] in names:
            total += rec['price']
    return total


def main(file1, file2, key1, key2):
    data1 = get_file(file1)
    data2 = get_file(file2)
    data1.sort(key=lambda x: x[key1])
    data2.sort(key=lambda x: x[key2])

    result = inner_join(data1, data2, key1, key2)
    pprint(calc_total(result, ['Barry', 'Steve']))  # The total is 19.5
    pprint(len(result))  # The length is 6
    return result


if __name__ == "__main__":
    main('data/customers.json', 'data/orders.json', 'cid', 'customer_id')
