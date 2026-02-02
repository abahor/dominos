from collections import Counter


def create_domino_set():
    return [(i, j) for i in range(7) for j in range(i, 7)]

total = create_domino_set()
print(total)
left = set(total)
player_1 = []
cannot_have = {
    1: set(),
    2: set(),
    3: set(),
    4: set(),
}
played_by_player = {
    1: set(),
    2: set(),
    3: set(),
    4: set()
}


for i in range(1,8):
    x = int(input(f"Tile {i}\n"))
    y = int(input(f"Tile {i}\n"))
    player_1.append(tuple(sorted([x,y])))


def first_tile():
    possible_plays = [i for i in player_1 if i[0] == i[1]]
    if possible_plays:
        print(f"Play {max(possible_plays)}")
        player_1.remove(max(possible_plays))
        left.remove(max(possible_plays))
        played_by_player[1].add(max(possible_plays))
    else:
        print("Play any tile you have")
        x = int(input("Enter the tile you played num 1"))
        y = int(input("Enter the tile you played num 2"))
        player_1.remove(tuple(sorted([x,y])))
        left.remove(tuple(sorted([x,y])))
        played_by_player[1].add(tuple(sorted([x,y])))




def check_what_to_play():
    if len(left) == 28:
        first_tile()
        return

    end_1 = int(input("Enter end num 1:\n"))
    end_2 = int(input("Enter end num 2:\n"))
    possible_plays = set()
    if end_1 in cannot_have[1] and end_2 in cannot_have[1]:
        print("No Possible play")
        return
    for i in player_1:
        if end_1 in i or end_2 in i:
            possible_plays.add(i)
    print(len(possible_plays))
    if len(possible_plays) == 0:
        print("No possible plays")
        cannot_have[1].add(end_1)
        cannot_have[1].add(end_2)
        return
    # if len(po)
    ends = [end_1, end_2]
    calculate_the_best_tile(possible_plays, ends)


def calculate_the_best_tile(possible_plays, ends):
    if len(player_1) == 1:
        print(f"Play ({player_1[0]})")
        print("YOU WON!!")
        return ""
    evaluate = {i: 0 for i in possible_plays}
    for tile in evaluate:
        a, b = tile
        score = max(evaluate_partner_support(a, b, ends[0]),
                    evaluate_partner_support(a, b, ends[1]))
        score += max(evaluate_block_opponents(a,b, ends[0]),
                     evaluate_block_opponents(a,b, ends[1]))
        score += max(evaluate_maintaining_control(possible_plays,a, b, ends[0]),
                     evaluate_maintaining_control(possible_plays,a, b, ends[1]))
        evaluate[tile] = score

    max_key = max(evaluate, key=evaluate.get)
    print(f"Best Domino {max_key}")
    left.remove(max_key)
    player_1.remove(max_key)
    played_by_player[1].add(max_key)
    return max_key

def evaluate_partner_support(a, b, end):
    if a == end:
        new_end = b
    elif b == end:
        new_end = a
    else:
        return  -1000 # illegal


    if new_end in cannot_have[3]:
        score = -50
    else:
        score = 40
        if a == b:
            score += 10
    # ------ WILL ADD FREQUENCY TO HELP PARTNER
    return score


def evaluate_block_opponents(a, b, end):
    if a == end:
        new_end = b
    elif b == end:
        new_end = a
    else:
        return -100

    if new_end in cannot_have[2]:
        score = 50
    else:
        score = 10

    if a == b:
        score += 10
    return score

def count_number(tiles, number):
    counter = Counter()
    for a, b in tiles:
        counter[a] += 1
        counter[b] += 1
    return counter[number]


def evaluate_maintaining_control(tiles,a, b, end):
    if a == end:
        new_end = b
    elif b == end:
        new_end = a
    else:
        return -1000

    freq = count_number(tiles,new_end)
    return freq*5

def record_other_players():
    p = int(input("Enter player number, you're player 1\n"))
    x = int(input("played tile\n"))
    y = int(input("played tile\n"))
    tile = tuple(sorted([x, y]))
    played_by_player[p].add(tile)
    left.discard(tile)

def record_players_blockers():
    p = int(input("Enter player number, You're player number 1:\n"))
    end_tile_num_1 = int(input("End number 1:\n"))
    end_tile_num_2 = int(input("End number 2:\n"))
    update_players_blockers(p, end_tile_num_1, end_tile_num_2)


def update_players_blockers(p, end_1, end_2):
    cannot_have[p].add(end_1)
    cannot_have[p].add(end_2)


def game():
    i = int(input("Your turn 0 or someone else 1, if someone passed enter 2:\n"))
    while i != 3:
        if i == 0:
            "CHECK WHAT TO PLAY"
            check_what_to_play()
            # pass
        elif i == 1:
            record_other_players()
        elif i == 2:
            record_players_blockers()
        i = int(input("your turn 0 or someone else 1, if someone passed enter 2:\n"))

game()