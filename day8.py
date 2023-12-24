def solve_part2_smork(network: dict, sequence: list[str]) -> int:
    # Tried running this for 2 days straight and it never finished, but
    # I still believe this works given enough time.
    positions = [key for key in network.keys() if key.endswith("A")]
    steps2: int = 0
    while [pos for pos in positions if not pos.endswith("Z")]:
        direction = sequence[steps2 % len(sequence)]
        for idx, pos in enumerate(positions):
            positions[idx] = network[pos][direction]
        steps2 += 1
    return steps2


def get_position_cycle(network: dict, sequence: list[str], position: str):
    step: int = 0
    net_to_seq_steps: dict[str, list[int]] = {position: [step]}
    history: list[str] = [position]

    while not [
        item
        for _, item in net_to_seq_steps.items()
        if len(set(item)) != len(item)
    ]:
        direction = sequence[step % len(sequence)]
        position = network[position][direction]
        step += 1
        history.append(position)
        net_to_seq_steps.setdefault(position, []).append(step % len(sequence))

    yield step

    for idx in range(step % len(sequence), len(history), len(sequence)):
        if history[idx] == position:
            yield idx
            break
    else:
        raise ("I did an ucky wucky fucky uwu")

    z_steps: list[int] = [
        idx for idx, pos in enumerate(history) if pos.endswith("Z")
    ]
    # Seems to only be one z instance per cycle
    yield z_steps[0]


def solve_part2_smart(network: dict, sequence: list[str]) -> int:
    start_positions = [key for key in network.keys() if key.endswith("A")]

    for position in start_positions:
        step, idx, z_step = get_position_cycle(network, sequence, position)
        print(step, idx, z_step)


def solve(in_data: list[str]):
    sequence: str = in_data[0].strip()
    network: dict[str, dict[str, str]] = {}
    for line in in_data[1:]:
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

    return steps, solve_part2_smart(network, sequence)


with open("day8.input", "r") as file:
    print(solve(file.readlines()))
