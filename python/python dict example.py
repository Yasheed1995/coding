#!/usr/bin/python

animal_shop = {'Mud_horse': 12, 'dog': 20, 'elephant': 99, 'white_dolphin': 87}
# access

print animal_shop['dog']
# print animal_shop['dolphin']

# update


# del


#animal_shop.clear()
# print animal_shop

# animal_shop = {'Mud_horse': 12, 'dog': 20, 'elephant': 99, 'Mud_horse': 1222, 'white_dolphin': 87}
# print animal_shop['Mud_horse']

# animal_shop = {['Mud_horse']: 12, 'dog': 20, 'elephant': 99, 'Mud_horse': 1222, 'white_dolphin': 87}
"""
# map
print animal_shop.values()
# 30.06

animal_shop_NT = map(lambda x: (30.06 * x), animal_shop.values())
print animal_shop_NT

animal_shop2 = {'Mud_horse': 34, 'dog': 12, 'elephant': 77, 'white_dolphin': 78}
animal_shop3 = {'Mud_horse': 6, 'dog': 4, 'elephant': 55, 'white_dolphin': 47}

animal_shop_avg = dict((key, value) for key, value in zip(animal_shop.keys(), map(lambda x, y, z: float(x + y + z)/3, animal_shop.values(), animal_shop2.values(), animal_shop3.values())))
print animal_shop_avg 
"""
'''
animal_shop4 = {'Mud_horse': 34, 'cat': 12, 'Africa_elephant': 77, 'white_dolphin': 78}
print set(animal_shop.keys()).intersection(set(animal_shop4.keys()))
print set(animal_shop.keys()).symmetric_difference(set(animal_shop4.keys()))
print set(animal_shop.keys()).difference(set(animal_shop4.keys()))
print set(animal_shop.keys()).union(set(animal_shop4.keys()))
'''

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print zip(a, b)
