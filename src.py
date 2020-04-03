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

    return list(map(line_to_data, lines[1:]))

def solve(data):
    mintimestamp, maxtimestamp = data[0][0], data[0][0]
    minlat, maxlat = data[0][1], data[0][1]
    minlng, maxlng = data[0][2], data[0][2]
    maxalt = data[0][3]

    for timestamp, lat, lng, alt in data:
        if timestamp < mintimestamp: mintimestamp = timestamp
        if timestamp > maxtimestamp: maxtimestamp = timestamp

        if lat < minlat: minlat = lat
        if lat > maxlat: maxlat = lat

        if lng < minlng: minlng = lng
        if lng > maxlng: maxlng = lng

        if alt > maxalt: maxalt = alt

    return [ 
        [mintimestamp, maxtimestamp],
        [minlat, maxlat],
        [minlng, maxlng],
        [maxalt]
  ]

for level in range(5):
    data = read(base_input + str(level + 1) + ".in")
    solution = solve(data)
    print_solution(solution)