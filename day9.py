from functools import reduce


def extrapolate(in_data: list[int]) -> list[int]:
    out_data: list[int] = []
    for idx in range(len(in_data) - 1):
        out_data.append(in_data[idx + 1] - in_data[idx])

    return out_data


def solve(in_data: list[str]) -> int:
    result: int = 0
    result2: int = 0
    for line in in_data:
        values = [int(v) for v in line.split()]
        lists: list[list[int]] = []
        while [x for x in values if x != 0]:
            lists.append(values)
            values = extrapolate(values)

        result += reduce(lambda a, b: a + b[-1], lists, 0)
        result2 += reduce(lambda a, b: b[0] - a, reversed(lists), 0)

    return result, result2


with open("day9.test_input", "r") as file:
    assert solve(file.readlines()) == (114, 2)

with open("day9.input", "r") as file:
    print(solve(file.readlines()))
