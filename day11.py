from functools import reduce


def expand_universe(in_data: list[str]) -> list[str]:
    out_data = [s.strip() for s in in_data]

    empty_rows = [idx for idx, line in enumerate(out_data) if "#" not in line]
    empty_cols = reduce(
        lambda a, b: [x for x in a if b[x] != "#"],
        out_data,
        [idx for idx, _ in enumerate(out_data[0])],
    )

    for idx, line in enumerate(out_data):
        temp = list(line)
        for col in reversed(empty_cols):
            temp.insert(col, ".")
        out_data[idx] = "".join(temp)

    for row in reversed(empty_rows):
        out_data.insert(row, "." * len(out_data[0]))

    return out_data


def solve(in_data: list[str]) -> int:
    result: int = 0
    galaxies: list[tuple[int, int]] = []
    for y, line in enumerate(expand_universe(in_data)):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))

    for idx, this_galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[idx + 1 :]:
            x1, y1 = this_galaxy
            x2, y2 = other_galaxy
            result += abs(x1 - x2) + abs(y1 - y2)

    return result


with open("day11.input", "r") as file:
    print(solve(file.readlines()))
