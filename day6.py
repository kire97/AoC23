import re

from dataclasses import dataclass
from functools import reduce


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
        # -x² = 356 - 49x
        # x² = -(356 - 49x)
        # x² = (49x - 356)
        # x = sqrt(49x - 356)
        # fuck it, I smork
        winnings: int = 0
        for ms in range(record.time):
            if (record.time - ms) * ms > record.distance:
                winnings += 1

        result *= winnings
    return result


def solve(in_data: list[str]) -> int:
    times = re.findall(r"\d+", in_data[0])
    distances = re.findall(r"\d+", in_data[1])
    assert len(times) == len(distances)
    records: list[Record] = [
        Record(int(times[i]), int(distances[i])) for i, _ in enumerate(times)
    ]

    result = solve_records(records)
    result2 = solve_records(
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
