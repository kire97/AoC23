def get_next(
    row: int, col: int, direction: str, in_data: list[str]
) -> dict[str, str]:
    bends = {
        "|": ("N", "S"),
        "-": ("W", "E"),
        "J": ("N", "W"),
        "L": ("N", "E"),
        "7": ("S", "W"),
        "F": ("S", "E"),
    }
    rev_dir = {"N": "S", "S": "N", "E": "W", "W": "E"}
    bend_to_route = {
        k: {rev_dir[v1]: v2, rev_dir[v2]: v1} for k, (v1, v2) in bends.items()
    }

    neighbours = {
        "N": (row - 1, col),
        "S": (row + 1, col),
        "W": (row, col - 1),
        "E": (row, col + 1),
    }

    row_idx, col_idx = neighbours[direction]
    try:
        new_direction = bend_to_route[in_data[row_idx][col_idx]][direction]
    except KeyError:
        return (row_idx, col_idx), None

    return (neighbours[direction], new_direction)


def solve(in_data: list[str]) -> int:
    # Just getting the start position
    row_idx, _ = [x for x in enumerate(in_data) if "S" in x[1]][0]
    col_idx, _ = [x for x in enumerate(in_data[row_idx]) if x[1] == "S"][0]

    direction: str = "N"
    steps: int = 0

    while in_data[row_idx][col_idx] != "S" or steps == 0:
        (row_idx, col_idx), direction = get_next(
            row_idx, col_idx, direction, in_data
        )
        steps += 1

    return steps // 2


with open("day10.input", "r") as file:
    print(solve(file.readlines()))
