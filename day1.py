with open('day1.input', mode='r') as file:
    result: int = 0
    for line in file.readlines():
        numbers = [c for c in line if c.isnumeric()]
        result += int(f'{numbers[0]}{numbers[-1]}')

    print(result)
