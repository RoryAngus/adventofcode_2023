import re
import os
import pandas as pd

pd.set_option("display.max_rows", 1001)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

_conversion_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_all_locs(num_to_find, string_to_look_in):
    # return [(i.start(), i.end()) for i in re.finditer(num_to_find, string_to_look_in)]
    return [(i.start()) for i in re.finditer(num_to_find, string_to_look_in)]


numbers_to_find = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

path = "C:\\Users\\RoryAngus\\Documents\\CodeCommit\\data-science-tools\\archive\\2023-12-01_rory_aoc\\01"
os.chdir(path)
df = pd.read_csv(r"data.txt", skiprows=0, header=None)  # , nrows=20)

print(f"df size: {len(df)}")
df.columns = ["data"]

print("\n\n~~~~~~~~~~~~~part b~~~~~~~~~~~~\n\n")


for number in numbers_to_find:
    print(f"working on number: {number}")
    df[number] = df["data"].map(lambda x: find_all_locs(number, x))
print(df.head(20))


def inject_num(
    string_to_inject, number_to_inject, positions_to_inject_into, conversion_dict
):
    injected_string = string_to_inject
    num_as_int = conversion_dict.get(number_to_inject)
    print(f"num_as_int; {num_as_int}")

    if positions_to_inject_into:
        for go_around, injection_position in enumerate(positions_to_inject_into):
            print(f"go_around: {go_around} - injected_string: {injected_string}")
            injected_string = (
                injected_string[:injection_position]
                + num_as_int
                + injected_string[injection_position + 1 :]
            )
            print(f"go_around: {go_around} - injected_string: {injected_string}")
    return injected_string


# numbers_to_find = ["one"]

for number in numbers_to_find:
    print(f"working on number: {number}")
    df["data"] = df.apply(
        lambda x: inject_num(x["data"], number, x[number], _conversion_dict), axis=1
    )
print(df.head(50))

## now i have put in the corresponding number in the first position that the nubmer starts

df["numbers_only"] = df["data"].str.replace("[a-zA-Z]", "")
df["first_num"] = df["numbers_only"].str.strip().str[0]
df["last_num"] = df["numbers_only"].str.strip().str[-1]
df["new_num"] = df["first_num"] + df["last_num"]
df["new_num_int"] = pd.to_numeric(df["new_num"], errors="coerce")
print(df.head(50))
print(f'the sum of the numbers is: {df["new_num_int"].sum()}')
