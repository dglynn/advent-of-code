#!/usr/bin/python
import re
# Day 1 : https://adventofcode.com/2023/day/1
# Problem 1

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the
# Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order)
# to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

# Problem 2

# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with
# letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

def solve(filename, solver):
    """
    filename: is a string
    solver: is a function
    """
    sum = 0
    with open(filename, "r") as reader:
        for line in reader.readlines():
            digits = solver(line.strip())

            num = int("".join([digits[0], digits[-1]]))
            sum += num
    return sum



def solver_1(line):
    return [*filter(lambda x: x <= '9' and x >= '0', line)]

text_to_number = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }

def solver_2(line):
    """ input: a string of line
        output: a list of number representation strings

        E.g.,
        solver_2("one3twone") => ["1", "3", "2", "1"]
    """
    search_pattern = "(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))"
    matched_numbers = re.findall(search_pattern, line)
    convert_function = lambda key: text_to_number.get(key, key)

    return [*map(convert_function, matched_numbers)]

if __name__ == "__main__":
    # test with the example string
    test_cases = [("problem1: test1", "example1_input", solver_1, 142), ("problem1: test2", "question1_input", solver_1, 54990),
                  ("problem2: test1", "example2_input", solver_2, 281), ("problem2: test2", "question1_input", solver_2, 54473)
    ]

    for (desc, input_file, solver, expected_output) in test_cases:
        print(desc)
        actual = solve(input_file, solver)
        assert expected_output == actual, f"Expected: {expected_output}, Got: {actual}"
        print("pass!")
