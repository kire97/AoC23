import re


def in_range(
    xy_positions: list[tuple[int, int]],
    x_range: tuple[int, int],
    y_range: tuple[int, int],
) -> bool:
    for x, y in xy_positions:
        if not (x >= x_range[0] and x <= x_range[1]):
            continue
        if not (y >= y_range[0] and y <= y_range[1]):
            continue
        return True
    else:
        return False


def solve(in_data: list[str]) -> int:
    result: int = 0
    special_positions: list[tuple[int, int]] = []
    for row_idx, line in enumerate(in_data):
        for col_idx, char in enumerate(line.strip()):
            if not char.isnumeric() and char != ".":
                special_positions.append((row_idx, col_idx))

    for row_idx, line in enumerate(in_data):
        for match in re.finditer(r"\d+", line):
            value = int(match.group(0))
            col_range = (match.start(0) - 1, match.end(0))
            row_range = (row_idx - 1, row_idx + 1)
            if in_range(special_positions, row_range, col_range):
                result += value

    return result


with open("day3.input", "r") as file:
    print(solve(file.readlines()))
