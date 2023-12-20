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


def translate_seed_ranges(
    pos_to_ranges: dict[str, list[tuple[int, int]]],
    dest_map: DestinationMap,
):
    source: str = dest_map.source
    target: str = dest_map.target

    pos_to_ranges[target] = []

    while pos_to_ranges[source]:
        # print(len(pos_to_ranges[target]))
        source_range = pos_to_ranges[source].pop()
        start, end = source_range
        for map_range in dest_map.offset_list:
            if start < map_range.start and map_range.end < end:
                pos_to_ranges[source].append((start, map_range.start - 1))
                pos_to_ranges[source].append((map_range.end + 1, end))
                pos_to_ranges[target].append(
                    (
                        map_range.offset + map_range.start,
                        map_range.offset + map_range.end,
                    )
                )
                break
            if map_range.start <= start and end <= map_range.end:
                pos_to_ranges[target].append(
                    (start + map_range.offset, end + map_range.offset)
                )
                break
            if map_range.start <= start <= map_range.end:
                pos_to_ranges[target].append(
                    (
                        start + map_range.offset,
                        map_range.end + map_range.offset,
                    )
                )
                pos_to_ranges[source].append((map_range.end + 1, end))
                break
            if map_range.start <= end <= map_range.end:
                pos_to_ranges[source].append((start, map_range.start - 1))
                pos_to_ranges[target].append(
                    (
                        map_range.start + map_range.offset,
                        end + map_range.offset,
                    )
                )
                break
        else:
            pos_to_ranges[target].append(source_range)

    return target


def solve(in_data: list[str]) -> int:
    seeds: list[int] = []
    mapper: dict[DestinationMap] = {}
    current_map: DestinationMap = None
    for line in in_data:
        numbers: list[int] = [int(s) for s in re.findall(r"\d+", line)]
        if line.startswith("seeds:"):
            seeds = numbers
            seed_ranges = [
                (a, a + numbers[i + 1] - 1)
                for i, a in enumerate(numbers)
                if not i % 2
            ]
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

    position = "seed"
    pos_to_ranges: dict[str, list[tuple[int, int]]] = {"seed": seed_ranges}
    while position in mapper.keys():
        position = translate_seed_ranges(pos_to_ranges, mapper[position])

    result = reduce(lambda a, b: a if a < b else b, locations)
    result2 = reduce(
        lambda a, b: a if a[0] < b[0] else b, pos_to_ranges["location"]
    )[0]

    return result, result2


with open("day5.input", "r") as file:
    print(solve(file.readlines()))
