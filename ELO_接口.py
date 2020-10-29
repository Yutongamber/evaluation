
'''
evaluate return function
input:
agents_id: ['1','2']
results: {'1': '{"1": 1, "2": 0, "sum_return": 1}', '2': '{"1": 0, "2": 1, "sum_return": 1}'}
# value : json.loads()
env_id: 5
return: [1000,1000]

output:
return: [x, y]
'''

import json

def eval_elo(agents_id, results, env_id, score_current, K = 42):
    ##########################################
    # tell who wins
    agents_0, agents_1 = agents_id[0], agents_id[1]
    return_0 = json.loads(results[agents_0])['sum_return']
    return_1 = json.loads(results[agents_1])['sum_return'] # to check: sum_return
    if return_0 > return_1:
        W_0, W_1 = 1, 0
    elif return_0 < return_1:
        W_0, W_1 = 0, 1
    elif return_0 == return_1:
        W_0, W_1 = 0.5, 0.5 # to check: whether includes all situations

    ##########################################
    # update score
    P_0 = (1 + 10 ** ((score_current[1] - score_current[0]) / 400.0)) ** -1
    P_1 = (1 + 10 ** ((score_current[0] - score_current[1]) / 400.0)) ** -1 # equal to 1 - P_0
    score_update0 = score_current[0] + K * (W_0 - P_0)
    score_update1 = score_current[1] + K * (W_1 - P_1)

    return [score_update0, score_update1]



'''
sample function
input:
{5: {1:1000,2:1200}, 4: {2:1000}}


output:
# key = ['agents','env_id']
values = [['1,2',2],['2,3',3],['1,5',1]]
'''

if __name__ == "__main__":
    agents_id = ['1', '2']
    results = {'1': '{"1": 1, "2": 0, "sum_return": 1}', '2': '{"1": 0, "2": 1, "sum_return": 0}'}
    env_id = 5
    score_current = [900, 1000]

    score = eval_elo(agents_id, results, env_id, score_current, K=42)
    print(score)

'''
comments: 
1. env_id: 没用到
2. double check 输入格式
3. K: 超参；可调

'''