import re


def looper(a: list[int], b: list[int]) -> int:
    matches: int = 0
    for value in a:
        matches += int(value in b)
    return matches


def solve(in_data: list[str]) -> int:
    result: int = 0
    for line in in_data:
        game_idx = int(line[4:8])
        line_parts = line.split(":")[1].split("|")
        win_nrs = re.findall(r"\d+", line_parts[0])
        our_nrs = re.findall(r"\d+", line_parts[1])

        if matches := looper(win_nrs, our_nrs):
            result += 2 ** (matches - 1)

    return result


with open("day4.input", "r") as file:
    print(solve(file.readlines()))
