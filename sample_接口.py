
'''
Coder：Yutongamber
function: sample

# sample function 2
# input:
# {5: {1:1000,2:1200}, 4: {2:1000}}
# 4,5: 代表 env
# {1:1000, 2:1200}: 1,2 玩家 1000，1200：当前分
# 输入可乱序
# 如果一个人的话，不加入pair

# output:
# key = ['agents','env_id']
# pairs = [['1,2',2],['2,3',3],['1,5',1]]
'''

'''
sample 1
# input:
# {5: {1:1000, 2:1200, 3:1000}}
# output:
# ['2,3',5]
'''

import operator

def tell_even(value): # to check: what if 没有元素
    even = True
    if value % 2 == 0: # 偶数
        return even
    else:
        return False

def sort(dictt):
    ###############################################
    # 字典按value排序
    # reverse=True表示按降序排列，若不写，则默认升序排列。
    sorted_dictt = sorted(dictt.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dictt = dict(sorted_dictt) # list 转 dict [(3, 4), (4, 3), (1, 2), (2, 1), (0, 0)]
    return sorted_dictt # {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

def sample_player1(list, sub_id):
    pairs = []
    for keys, values in list.items():
        values = sort(values)
        length = len(values)
        all_players_env = []
        for key_ in values.keys():
            all_players_env.append(key_)
        if all_players_env.index(sub_id) == 0:
            pair_ = (str(all_players_env[all_players_env.index(sub_id)+1]), str(sub_id))
            pairs.append([','.join(pair_), keys])
        else:
            pair_ = (str(sub_id), str(all_players_env[all_players_env.index(sub_id) - 1]))
            pairs.append([','.join(pair_), keys])
        return pairs


def sample_player2(list):
    ###############################################
    pairs = []
    for keys, values in list.items():
        values = sort(values)
        length = len(values)
        all_players_env = []
        if length > 1:            # 排除一个人情况
        ###########################################
            if tell_even(length): # 偶数
                for key_ in values.keys():
                    all_players_env.append(key_)
                for i in range(int(length/2)):
                    ii = 2 * i
                    pair_ = (str(all_players_env[ii]), str(all_players_env[ii+1]))
                    pairs.append([','.join(pair_), keys])
            else:                 # 奇数
                for key_ in values.keys():
                    all_players_env.append(key_)
                for i in range(int((length-1)/2)):
                    ii = 2 * i + 1
                    pair_ = (str(all_players_env[ii]), str(all_players_env[ii+1]))
                    pairs.append([','.join(pair_), keys])
                pair_ = (str(all_players_env[0]), str(all_players_env[1]))
                pairs.append([','.join(pair_), keys])
    return pairs



if __name__ == "__main__":
    # 测试list # list可乱序
    list = {4: {2: 1000, 1: 900, 3: 800, 4: 600}}
    list = {5: {1: 1000, 2: 800, 3: 900}}
    list = {5: {1: 1000, 2: 1200, 3: 900}, 4: {2: 1000, 1: 900, 3: 800, 4: 600}}
    list = {5: {1: 1000, 2: 1200, 3: 900}, 4: {2: 1000, 1: 900, 3: 800, 4: 600}, 3:{1:1000}}
    list1 = {5: {1: 1000, 2: 800, 3: 900}}
    pairs = sample_player2(list)
    pairs1 = sample_player1(list1, 1)
    print(pairs)
    print(pairs1)


'''
comments:
1. double check input and output
2. to check: list里面没有人的时候? 
'''