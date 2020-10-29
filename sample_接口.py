'''
sample function
input:
{5: {1:1000,2:1200}, 4: {2:1000}}


output:
# key = ['agents','env_id']
values = [['1,2',2],['2,3',3],['1,5',1]]
'''

'''
sample function
input:
{5: {1:1000,2:1200,3:900}, 4: {2:1000, 1:900}}

output:
# key = ['agents','env_id']
values = [['1,3',5],['1,2',5],['1,2',4]]

'''

import numpy as np

def tell_even(value): # to check: what if 没有元素
    even = True
    if value % 2 == 0: # 偶数
        return even
    else:
        return False

def sample_player(list):
    ###################################
    num_env = len(list)
    pairs = []
    even = True
    for keys, values in list.items():
        length = len(values)
        if tell_even(length):





if __name__ == "__main__":
    list = {5: {1:1000,2:1200,3:900}, 4: {2:1000, 1:900}}



'''
comments:
1. double check input and output
'''