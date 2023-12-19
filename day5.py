import re

from functools import reduce
from dataclasses import dataclass, field


@dataclass
class RangeOffset:
    start: int
    end: int
    offset: int


@dataclass
class DestinationMap:
    source: str
    target: str
    offset_list: list[RangeOffset] = field(default_factory=list)


def translate_seed(
    value: int, current_position: str, mapper: dict[DestinationMap]
):
    if current_position not in mapper.keys():
        return value
    dest_map = mapper[current_position]

    for offset in dest_map.offset_list:
        if offset.start <= value <= offset.end:
            value += offset.offset
            break

    return translate_seed(value, dest_map.target, mapper)


def solve(in_data: list[str]) -> int:
    seeds: list[int] = []
    mapper: dict[DestinationMap] = {}
    current_map: DestinationMap = None
    for line in in_data:
        numbers: list[int] = [int(s) for s in re.findall(r"\d+", line)]
        if line.startswith("seeds:"):
            seeds = numbers
        if "map:" in line:
            source = line.split("-")[0]
            destination = line.split("-")[-1][:-6]
            current_map = DestinationMap(source, destination)
            mapper[current_map.source] = current_map
        if current_map and numbers:
            offset = numbers[0] - numbers[1]
            start = numbers[1]
            end = numbers[1] + numbers[2] - 1
            current_map.offset_list.append(RangeOffset(start, end, offset))

    locations: list[int] = []
    for seed in seeds:
        locations.append(translate_seed(seed, "seed", mapper))

    return reduce(lambda a, b: a if a < b else b, locations)


with open("day5.input", "r") as file:
    print(solve(file.readlines()))
