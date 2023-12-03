def reduce_str(input: str):
    result = input
    string_to_int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, }

    for k, v in string_to_int.items():
        slices = result.split(k)
        for slice in slices[:-1]:
            result += f'{slice}{v}'
        result += f'{slices[-1]}'
    return result

def solve(input: list[str]):
    result: int = 0

    for line in input:

        numbers = [c for c in reduce_str(line) if c.isnumeric()]

        result += int(f'{numbers[0]}{numbers[-1]}')



    return result
    
with open('day1.input', mode='r') as file:
    print(solve(file.readlines()))
