def get_hand_value(line: str):
    hand: str = line.split()[0]
    hand_value = 0

    card_to_value = {
        "2": 0,
        "3": 1,
        "4": 2,
        "5": 3,
        "6": 4,
        "7": 5,
        "8": 6,
        "9": 7,
        "T": 8,
        "J": 9,
        "Q": 10,
        "K": 11,
        "A": 12,
    }
    for i, card in enumerate(reversed(hand)):
        hand_value += (13**i) * card_to_value[card]

    copies_list: list[int] = []
    while hand:
        card = hand[0]
        copies_list.append(hand.count(card))
        hand = hand.replace(card, "")

    hand_type: int
    match len(copies_list):
        case 5:
            # High Card
            hand_type = 0
        case 4:
            # One Pair
            hand_type = 1
        case 3:
            if 3 not in copies_list:
                # Two Pair
                hand_type = 2
            else:
                # Three of a kind
                hand_type = 3
        case 2:
            if 3 in copies_list:
                # Full house
                hand_type = 4
            else:
                # Four of a kind
                hand_type = 5
        case 1:
            # Five of a kind
            hand_type = 6

    return (13**5) * hand_type + hand_value


def solve(in_data: list[str]):
    result: int = 0
    for idx, line in enumerate(sorted(in_data, key=get_hand_value)):
        bid = int(line.split()[1])
        result += bid * (idx + 1)

    return result


with open("day7.input", "r") as file:
    print(solve(file.readlines()))
