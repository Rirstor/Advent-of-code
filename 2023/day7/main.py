import numpy as np
from functools import cmp_to_key

data = np.array([line.split() for line in open("day7/input.txt")])

ref = "AKQT98765432J"


def process_card(card):
    output2 = dict()
    for key in card:
        if key in output2:
            output2[key] += 1
        else:
            output2[key] = 1
    if "J" in output2 and len(output2.keys()) != 1:
        value = output2.pop("J")
        if max(output2.values()) == 1:
            for k in ref:
                if k in output2:
                    output2[k] += 1
                    break
        else:
            key = [key for key in output2 if output2[key] == max(output2.values())]
            if len(key) != 1:
                for k in ref:
                    if k in key:
                        output2[k] += value
                        break
            else:
                key = key[0]
                output2[key] += value
    return output2


ref = {key: value for key, value in zip(ref, (np.arange(len(ref)) + 1001).astype(str)[::-1])}

cards = [process_card(card) for card in data[:, 0]]


def sorter(idx):
    return int("".join(ref[c] for c in data[idx, 0]))


output = 0
nb_cards_max = [max(card.values()) for card in cards]
nb_cards_diff = [len(card) for card in cards]
rank = data.shape[0]
for nb_cards, different_cards in zip([5, 4, 3, 3, 2, 2, 1], [1, 2, 2, 3, 3, 4, 5]):
    cards_oi = [i for i in range(len(cards)) if (nb_cards_max[i] == nb_cards) and (nb_cards_diff[i] == different_cards)]

    sorted_cards = sorted(cards_oi, key=sorter, reverse=True)
    output += sum((rank - j) * int(data[i, 1]) for j, i in enumerate(sorted_cards))

    rank -= len(sorted_cards)
print(output)

data = [l.strip().split(' ') for l in open('day7/input.txt')]

def joker(a):
    return max(a, key=a.get)

def replace(a, o='AKQT98765432'):
    return a.replace('J', joker({c: a.count(c) for c in o}))

def score(a, b, o='AKQJT98765432'):
    return [max(b.count(c) for c in b), -len(set(list(b)))] + [-o.index(c) for c in a]

def win(a):
    return sum(int(b) * (i + 1) for i, (_, b) in enumerate(a))

print(win(sorted(data, key=lambda x: score(x[0], replace(x[0]), 'AKQT98765432J'))))