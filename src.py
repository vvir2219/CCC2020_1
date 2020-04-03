base_input = "./input/level2_"
base_output = "./output/level2_"

def line_to_data(line):
    data = line.split(',')
    data[0] = int(data[0])
    data[1] = float(data[1])
    data[2] = float(data[2])
    data[3] = float(data[3])
    data[6] = int(data[6])
    return data

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    return list(map(line_to_data, lines[1:]))

def solve(data):
    flights = {} # map from [start, destination] to a set of takeoff times

    for timestamp, lat, lng, alt, start, destination, takeoff in data:
        if ( start, destination ) not in flights:
            flights[( start, destination )] = set()

        flights[( start, destination )].add(timestamp)

    solution = [] # array of sorted (start, destination, len(flights))
    for start, destination in flights.keys():
        solution.append([start, destination, len(flights[(start, destination)])])

    return sorted(sorted(solution, key=lambda x: x[1]), key=lambda x: x[0])

def print_solution(solution, filename):
    with open(filename, "w") as f:
        print("\n".join(map(lambda line: " ".join(map(lambda y: str(y), line)), solution)), file=f)

for level in range(5):
    data = read(base_input + str(level + 1) + ".in")
    solution = solve(data)
    print_solution(solution, base_output + str(level + 1) + ".out")