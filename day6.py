import re

from dataclasses import dataclass
from functools import reduce
from math import ceil, floor


@dataclass
class Record:
    time: int
    distance: int


def solve_records(records: list[Record]) -> int:
    result: int = 1
    for record in records:
        # (49 - x)x = 356
        # (49 - x) = 356/x
        # 49x - x² = 356
        # -x² + 49x - 356 = 0
        # (-49 +- sqrt(49² + 4*356))/-2
        # (-49 +- sqrt(3825))/-2
        # (-49 +- sqrt(3825))/-2
        # fuck it, I smork
        winnings: int = 0
        for ms in range(record.time):
            if (record.time - ms) * ms > record.distance:
                winnings += 1

        result *= winnings
    return result


def solve_records_smart(records: list[Record]) -> int:
    result: int = 1
    # ax² + bx + c = 0
    # a = -1
    # b = 49
    # c = -356
    # (-b±√(b²-4ac))/(2a)
    for record in records:
        plus_minus = ((record.time**2) - (4 * record.distance)) ** 0.5
        lower = ceil((-record.time + plus_minus) / -2)
        upper = floor((-record.time - plus_minus) / -2)
        result *= 1 + upper - lower
    return result


def solve(in_data: list[str]) -> int:
    times = re.findall(r"\d+", in_data[0])
    distances = re.findall(r"\d+", in_data[1])
    assert len(times) == len(distances)
    records: list[Record] = [
        Record(int(times[i]), int(distances[i])) for i, _ in enumerate(times)
    ]

    result = solve_records_smart(records)
    result2 = solve_records_smart(
        [
            Record(
                int(reduce(lambda a, b: a + b, times)),
                int(reduce(lambda a, b: a + b, distances)),
            )
        ]
    )
    return result, result2


with open("day6.input", "r") as file:
    print(solve(file.readlines()))
