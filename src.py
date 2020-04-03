base_input = "./input/level1_"

for level in range(5):
    data = read(base_input + str(level + 1))
    solution = solve(data)
    print_solution(solution)