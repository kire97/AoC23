def solve(in_data: list[str]):
    sequence: str = in_data[0].strip()
    network: dict[str, dict[str, str]] = {}
    for line in in_data[2:]:
        key = line[0:3]
        left = line[7:10]
        right = line[12:15]
        network[key] = {"L": left, "R": right}

    position: str = "AAA"
    steps: int = 0
    while position != "ZZZ":
        direction = sequence[steps % len(sequence)]
        position = network[position][direction]
        steps += 1

    return steps


with open("day8.input", "r") as file:
    print(solve(file.readlines()))
