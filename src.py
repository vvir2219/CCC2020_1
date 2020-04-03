import math

base_input = "./input/level3_"
base_output = "./output/level3_"

R = 6371000
f_inv = 300.0
f = 0.0
e2 = 1 - (1 - f) * (1 - f)

def gps_to_ecef(latitude, longitude, altitude):
    # (lat, lon) in WSG-84 degrees
    # h in meters
    cosLat = math.cos(latitude * math.pi / 180)
    sinLat = math.sin(latitude * math.pi / 180)

    cosLong = math.cos(longitude * math.pi / 180)
    sinLong = math.sin(longitude * math.pi / 180)

    c = 1 / math.sqrt(cosLat * cosLat + (1 - f) * (1 - f) * sinLat * sinLat)
    s = (1 - f) * (1 - f) * c

    x = (R*c + altitude) * cosLat * cosLong
    y = (R*c + altitude) * cosLat * sinLong
    z = (R*s + altitude) * sinLat

    return x, y, z

def line_to_data(line):
    data = line.split(',')
    data[0] = float(data[0])
    data[1] = float(data[1])
    data[2] = float(data[2])
    return data

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    return list(map(line_to_data, lines[1:]))

def solve(data):

    solution = []
    for lat, lng, alt in data:
        solution.append(list(gps_to_ecef(lat, lng, alt)))

    return solution

def print_solution(solution, filename):
    with open(filename, "w") as f:
        print("\n".join(map(lambda line: " ".join(map(lambda y: str(y), line)), solution)), file=f)

def main():
    for level in range(5):
        data = read(base_input + str(level + 1) + ".in")
        solution = solve(data)
        print_solution(solution, base_output + str(level + 1) + ".out")

def example():
    print_solution(solve(read(base_input + "example.in")), base_output+"example.out")

main()