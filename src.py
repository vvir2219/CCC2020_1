base_input = "./input/level1_"

def line_to_data(line):
    data = line.split(',')
    data[0] = int(data[0])
    data[1] = float(data[1])
    data[2] = float(data[2])
    data[3] = float(data[3])
    return data

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    return map(line_to_data, lines[1:])


for level in range(5):
    data = read(base_input + str(level + 1) + ".in")
    solution = solve(data)
    print_solution(solution)