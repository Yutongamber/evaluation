from elopy import *
i = Implementation()
def demo():
    i = Implementation()

    # add a new player
    i.addPlayer("a", rating = 1000)
    i.addPlayer("b",rating= 1000)

    print(i.getPlayerRating("a"), i.getPlayerRating("b"))

    pair = 'a', 'b'
    i.recordMatch(pair, winner=None, draw=True)

    i.recordMatch("a","b",winner=None, draw=True)

    print(i.getRatingList())

    i.recordMatch("a","b",winner='a', draw=False)

    print(i.getRatingList())

    # add a new player
    i.addPlayer("c", rating = 1000)
    print(i.getPlayerRating("c"))
    i.recordMatch("a","c",winner='a', draw=False)
    print(i.getRatingList())


    # add a new player
    i.addPlayer("d", rating = 1000)
    print(i.getPlayerRating("c"))
    i.recordMatch("d","c",winner='c', draw=False)
    print(i.getRatingList())

    return i.getRatingList()

def sort_table(list):
    list = sorted(list,reverse=True, key = lambda list_ : list_[1])
    return list

def sample_player(list):
    # 每天sample 不同的玩家， 然后更新table
    num_players = len(list)
    if num_players % 2 == 0 : # 偶数  -->  每两个一比
        for i in range(int(num_players / 2)):
            ii = 2 * i
            result = battle(list[ii][0], list[ii+1][0]) # 对弈
            i.recordMatch(list[ii][0], list[ii+1][0], result) # @@@ to do: from result to tell_win
    else:  # 奇数 --> 每两个一比， 除去第一玩家
        for i in range(int((num_players-1)/2)):
            ii = 2 * (i+1)
            result = battle(list[ii][0], list[ii + 1][0])  # 对弈
            i.recordMatch(list[ii][0], list[ii + 1][0], result)  # @@@ to do: from result to tell_win
        result = battle(list[0][0], list[1][0])  # 对弈
        i.recordMatch(list[0][0], list[1][0], result)  # @@@ to do: from result to tell_win

    return i.getRatingList() # new list

if __name__ == "__main__":
    i = Implementation()
    list = demo()
    table = sort_table(list)
    print('sorted_table', table)




