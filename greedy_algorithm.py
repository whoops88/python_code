denominations = [1, 2, 5, 10, 20, 50, 100]
# 100p is £1

def return_change(change, denomination):
    to_give_back = [0] * len(denomination)
    for pos, coin in enumerate(reversed(denomination)):
        while coin <= change:
            change = change - coin
            to_give_back[pos] += 1
    return to_give_back


print(return_change(30, denominations))