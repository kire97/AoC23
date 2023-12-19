import re
from dataclasses import dataclass


@dataclass
class Card:
    matches: int
    copies: int = 1


def looper(a: list[int], b: list[int]) -> int:
    matches: int = 0
    for value in a:
        matches += int(value in b)
    return matches


def solve(in_data: list[str]) -> int:
    result: int = 0
    result2: int = 0
    cards: list[Card] = []
    for line in in_data:
        line_parts = line.split(":")[1].split("|")
        win_nrs = re.findall(r"\d+", line_parts[0])
        our_nrs = re.findall(r"\d+", line_parts[1])

        matches = looper(win_nrs, our_nrs)
        if matches:
            result += 2 ** (matches - 1)

        cards.append(Card(matches))

    for card_idx, card in enumerate(cards):
        for offset_idx in range(card.matches):
            cards[card_idx + offset_idx + 1].copies += card.copies
        result2 += card.copies

    return result, result2


with open("day4.input", "r") as file:
    print(solve(file.readlines()))
