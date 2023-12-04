import re
import os
import pandas as pd
from functools import reduce
from collections import OrderedDict

pd.set_option("display.max_rows", 1001)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
filename = "data.txt"
path = "C:\\Users\\RoryAngus\\Documents\\CodeCommit\\data-science-tools\\archive\\2023-12-01_rory_aoc\\03"
os.chdir(path)


def is_symbol(supplied_character):
    # test to see if the supplied character matches a symbol
    all_symbols = re.compile("[^\w\s\.]+")
    # output = all_symbols.match(supplied_character)
    return bool(all_symbols.match(supplied_character))


def all_locations(string_to_search, string_to_find):
    occurrences = re.finditer(string_to_find, string_to_search)
    res = reduce(lambda x, y: x + [y.start()], occurrences, [])
    return res


def update_positions(current_line_num_n_pos, length_of_line):
    return_var = {}
    for number_to_check, positions_of_number in current_line_num_n_pos.items():

        # make it a set to remove duplicates
        positions_of_number_set = set(positions_of_number)
        # print(number_to_check, positions_of_number_set)
        # need to add positions for the length of the number
        if len(number_to_check) > 0:
            # add items to list for each digit of the number for each entry in list
            for entry_in_list in positions_of_number:
                counter = 0
                for digit in list(number_to_check):
                    if entry_in_list + counter <= length_of_line:
                        positions_of_number_set.add(entry_in_list + counter)
                    # increments counter
                    counter += 1

                return_var.update({number_to_check: list(positions_of_number_set)})

    return return_var


def check_position_current_line(
    locations_of_number, current_line_actual, number_to_check
):
    result = False
    for current_location_to_check in locations_of_number:
        if current_location_to_check == 0:  # far left position
            # check left
            if is_symbol(current_line_actual[current_location_to_check + 1]):
                result = True
        elif (
            current_location_to_check == len(current_line_actual) - 1
        ):  # far right position
            # check left
            if is_symbol(current_line_actual[current_location_to_check - 1]):
                result = True
        else:
            # check left and right
            if is_symbol(current_line_actual[current_location_to_check - 1]):
                result = True
            if is_symbol(current_line_actual[current_location_to_check + 1]):
                result = True
        if result:
            valid_part_numbers.append(number_to_check)
            print(
                "!~~~~~~~~~~~~~~~~~~~ symbol matched current line !~~~~~~~~~~~~~~~~~~~"
            )
            print(
                f"number checked: {number_to_check}, it locations {locations_of_number},  current valid part numbers {valid_part_numbers}"
            )

            break


def check_position_other_line(
    locations_of_number, current_line_actual, other_line_actual, number_to_check
):
    result = False
    for current_location_to_check in locations_of_number:
        if current_location_to_check == 0:  # far left position
            # check forwards
            if is_symbol(other_line_actual[current_location_to_check]):
                result = True
            if is_symbol(other_line_actual[current_location_to_check + 1]):
                result = True
        elif (
            current_location_to_check == len(current_line_actual) - 1
        ):  # far right position
            # check backwards
            if is_symbol(other_line_actual[current_location_to_check - 1]):
                result = True
            if is_symbol(other_line_actual[current_location_to_check]):
                result = True
        else:
            # check 3 positions
            if is_symbol(other_line_actual[current_location_to_check - 1]):
                result = True
            if is_symbol(other_line_actual[current_location_to_check]):
                result = True
            if is_symbol(other_line_actual[current_location_to_check + 1]):
                result = True
        if result:
            valid_part_numbers.append(number_to_check)
            print("!~~~~~~~~~~~~~~~~~~~ symbol matched other line !~~~~~~~~~~~~~~~~~~~")
            print(
                f"number checked: {number_to_check}, it locations {locations_of_number},  current valid part numbers {valid_part_numbers}"
            )
            break


def check_current_line(current_line_in, valid_part_numbers):
    # check the current line against the next line

    # separate current line into the two parts
    current_line_actual = current_line_in[0]
    current_line_num_n_pos = current_line_in[1]

    current_line_num_n_all_pos = update_positions(
        current_line_num_n_pos, len(current_line_actual)
    )

    for number_to_check, locations_of_number in current_line_num_n_all_pos.items():
        print(
            f"\n\n ~~~~current line checking: {number_to_check}, at these locations: {locations_of_number})"
        )
        check_position_current_line(
            locations_of_number, current_line_actual, number_to_check
        )
    return valid_part_numbers


def check_other_line(current_line_in, other_line_in, valid_part_numbers):
    # check the current line against the next line

    # separate current line into the two parts
    current_line_actual = current_line_in[0]
    current_line_num_n_pos = current_line_in[1]
    # separate next line into the two parts
    other_line_actual = other_line_in[0]

    current_line_num_n_all_pos = update_positions(
        current_line_num_n_pos, len(current_line_actual)
    )

    for number_to_check, locations_of_number in current_line_num_n_all_pos.items():
        print(
            f"\n\n ~~~~other line: checking: {number_to_check}, at these locations: {locations_of_number})"
        )
        check_position_other_line(
            locations_of_number, current_line_actual, other_line_actual, number_to_check
        )
    return valid_part_numbers


# read file into my data structure {line_no: (line, locations_of_numbers)
counter = 0
control_loop = {}
processed_file = {}
valid_part_numbers = []
with open(filename) as file:
    for line in file:
        # split line into single characters
        line_tmp = list(line)
        # Don't want to keep the last character because it is a new line - use remove pop
        newline_discard = line_tmp.pop()

        # find the numbers in a line and their starting position
        # get the numbers first using split
        cleaned_line = re.sub("[^\w\s]", " ", line)
        numbers_only = cleaned_line.split()
        # print(cleaned_line)
        number_locations = {}
        for number in numbers_only:
            number_locations.update({number: all_locations(cleaned_line, number)})
        # print(number_locations)

        # build final data structure
        processed_file.update({counter: (line_tmp, number_locations)})
        control_loop.update({counter: number_locations})
        # increments counter
        counter += 1

# cleanup
del (
    line,
    file,
    cleaned_line,
    number,
    numbers_only,
    number_locations,
    line_tmp,
    newline_discard,
)

# ~~~~~~~~~~~ MAIN LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~

processed_file = OrderedDict(sorted(processed_file.items()))


for line_number, number_locations in control_loop.items():
    break


for line_number, current_line in processed_file.items():
    valid_part_numbers = []
    print(
        f"\n\n########################## processing line {line_number} ##########################"
    )
    # first line - cant look upwards
    if line_number == 0:
        # check the current line
        valid_part_numbers = check_current_line(current_line, valid_part_numbers)
        # check the line below only
        valid_part_numbers = check_other_line(
            current_line, processed_file.get(line_number + 1), valid_part_numbers
        )

        # last line cant look downwards
    elif line_number == counter - 1:
        # check the current line
        valid_part_numbers = check_current_line(current_line, valid_part_numbers)
        # check the line above only
        valid_part_numbers = check_other_line(
            current_line, processed_file.get(line_number - 1), valid_part_numbers
        )

        # all other lines can look up and down
    else:
        # check the current line
        valid_part_numbers = check_current_line(current_line, valid_part_numbers)
        # check the line above
        valid_part_numbers = check_other_line(
            current_line, processed_file.get(line_number - 1), valid_part_numbers
        )
        # check the line below
        valid_part_numbers = check_other_line(
            current_line, processed_file.get(line_number + 1), valid_part_numbers
        )

print(
    f"\n\nfinal valid part numbers {valid_part_numbers} \nand the sum is {sum(list(map(int, valid_part_numbers)))}"
)
