import re
from functools import reduce, partial


def solve(in_data: list[str]) -> int:
    result: int = 0
    result2: int = 0
    color_to_max = {"red": 12, "green": 13, "blue": 14}

    for line in in_data:
        game_idx = int(re.findall(r"(?<=Game )\d+", line)[0])

        def reducer(last: bool, value: int, max_value: int):
            return last and value <= max_value

        passed = True
        power = 1
        for color, value in color_to_max.items():
            rolls = re.findall(rf"\d+(?= {color})", line)
            rolls = [int(x) for x in rolls]
            passed = reduce(
                partial(reducer, max_value=value),
                rolls,
                passed,
            )
            power *= reduce(lambda a, b: a if a > b else b, rolls)
        if passed:
            result += game_idx
        result2 += power

    return result, result2


with open("day2.input", "r") as file:
    print(solve(file.readlines()))
