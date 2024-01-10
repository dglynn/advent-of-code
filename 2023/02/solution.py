#!/usr/bin/env python
import re

constraint = {"red": "12", "green": "13", "blue": "14"}

# game_results = [
#     [{"blue": "3", "red": "4"}, {"red": "1", "green": "2", "blue": "6"}, {"green": "2"}],
#     [{"blue": "1", "green": "2"}, {"green": "3", "blue": "4", "red": "1"}, {"green": "1", "blue": "1"}],
#     [{"green": "8", "blue": "6", "red": "20"}, {"blue": "5", "red": "4", "green": "13"}, {"green": "5", "red": "1"}],
#     [{"green": "1", "red": "3", "blue": "6"}, {"green": "3", "red": "6"}, {"blue": "15", "red": "14"}],
#     [{"red": "6", "blue": "1", "green": "3"}, {"blue": "2", "red": "1", "green": "2"}],
# ]

game_regex = r"^Game ([1-9][0-9]*)"
cube_regex = r"([1-9][0-9]*) (red|blue|green)"


def solve(file, solver):
    with open(file) as reader:
        parsed = []
        for line in reader.readlines():
            line = line.strip()
            game_number = re.findall(game_regex, line)
            cubes = [*map(parse_cubes, line.split(";"))]
            parsed.append(cubes)
    return solver(parsed)


def parse_cubes(input_str):
    cubes = re.findall(cube_regex, input_str)
    # cubes = [[('3', 'blue'), ('4', 'red')], [('1', 'red'), ('2', 'green'), ('6', 'blue')], [('2', 'green')]]
    return dict(map(lambda cube: (cube[1], cube[0]), cubes))


# [{'blue': '3', 'red': '4'}, {'red': '1', 'green': '2', 'blue': '6'}, {'green': '2'}]


def solve_1(game_results):
    # 1. parse input lines into game_results and constraint (omit)
    #
    # 2. use game_results and constraint to solve problem 1
    # output: game_index_count
    # for each result (and index of this item) in game_results:
    #   for each set in sets of results:
    #      check that the result in the set satisfy the constraint
    #      if it satisfies: game_index_count += (index of this result + 1)
    # return game_index_count
    valid_game_count = 0
    for index, game_result in enumerate(game_results, start=1):
        is_valid = True
        for cubes in game_result:
            # {'blue': '3', 'red': '4'}
            # constraint = {"red": "12", "green": "13", "blue": "14"}
            # keys must match before we compare the values
            for colour, max_count in constraint.items():
                count = cubes.get(colour, 0)
                if int(count) > int(max_count):
                    is_valid = False
        if is_valid:
            valid_game_count += index
    return valid_game_count


def solve_2(game_results):
    # [{"blue": "3", "red": "4"}, {"red": "1", "green": "2", "blue": "6"}, {"green": "2"}],
    # {"blue": "6", "red": "4", "green": "2"}
    sum_value = 0
    for index, game_result in enumerate(game_results, start=1):
        max_count = {"blue": 0, "red": 0, "green": 0}
        for cubes in game_result:
            for colour, current_max in max_count.items():
                # colour = blue, current_max = 0
                # cubes = {"blue": "3", "red": "4"}
                # print("colour: ", colour, "current_max:", current_max)
                current_cube_count = int(cubes.get(colour, 0))
                if current_cube_count > current_max:
                    max_count[colour] = current_cube_count
        # max_count = { "blue": 6, "red": 4, "green": 2 }
        mul_value = 1
        for value in max_count.values():
            # print("value: ", value, "mul_value: ", mul_value)
            mul_value = value * mul_value
            # print("value: ", value, "mul_value: ", mul_value)
        sum_value = sum_value + mul_value
    return sum_value


if __name__ == "__main__":
    # test with the example string
    print(solve("02_example1_input", solve_1))
    print(solve("question2_input", solve_1))
    print(solve("02_example1_input", solve_2))
    print(solve("question2_input", solve_2))
