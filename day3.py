import re
from dataclasses import dataclass, field
from functools import reduce


@dataclass
class SpecialCharacter:
    x_pos: int
    y_pos: int
    character: str
    neighbor_values: list[int] = field(default_factory=list)


def in_range(
    characters: list[SpecialCharacter],
    x_range: tuple[int, int],
    y_range: tuple[int, int],
) -> SpecialCharacter | None:
    for char in characters:
        x = char.x_pos
        y = char.y_pos
        if not (x >= x_range[0] and x <= x_range[1]):
            continue
        if not (y >= y_range[0] and y <= y_range[1]):
            continue
        return char
    else:
        return None


def solve(in_data: list[str]) -> int:
    result: int = 0
    result2: int = 0
    special_characters: list[SpecialCharacter] = []
    for row_idx, line in enumerate(in_data):
        for col_idx, char in enumerate(line.strip()):
            if not char.isnumeric() and char != ".":
                special_characters.append(
                    SpecialCharacter(col_idx, row_idx, char)
                )

    for row_idx, line in enumerate(in_data):
        for match in re.finditer(r"\d+", line):
            value = int(match.group(0))
            col_range = (match.start(0) - 1, match.end(0))
            row_range = (row_idx - 1, row_idx + 1)
            if char := in_range(special_characters, col_range, row_range):
                char.neighbor_values.append(value)
                result += value

    for char in special_characters:
        if char.character == "*" and len(char.neighbor_values) > 1:
            result2 += reduce(lambda a, b: a * b, char.neighbor_values)

    return result, result2


with open("day3.input", "r") as file:
    print(solve(file.readlines()))
