def reduce_str(in_data: str) -> str:
    result = in_data
    string_to_int = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    for k, v in string_to_int.items():
        # Have to append the number inbetween two
        # string versions in case another number overlaps
        result = result.replace(k, k + str(v) + k)
    return result


def solve(in_data: list[str]):
    result: int = 0

    for line in in_data:
        # part2
        numbered_line = reduce_str(line)

        numbers = [c for c in numbered_line if c.isnumeric()]
        result += int(f'{numbers[0]}{numbers[-1]}')

    return result


with open('day1.input', mode='r') as file:
    print(solve(file.readlines()))
