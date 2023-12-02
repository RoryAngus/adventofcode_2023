import re
import os
import pandas as pd

pd.set_option("display.max_rows", 1001)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 2000)

path = "C:\\Users\\RoryAngus\\Documents\\CodeCommit\\data-science-tools\\archive\\2023-12-01_rory_aoc\\02"
os.chdir(path)
df = pd.read_csv(r"data.txt", sep=":", skiprows=0, header=None)  # , nrows=20)
print(f"df size: {len(df)}")
df.columns = ["game", "data"]
df["id_int"] = df["game"].str.extract("(\d+)")  # .astype(int)

print("\n\n~~~~~~~~~~~~~part b~~~~~~~~~~~~\n\n")


def split_string(input_string, delimeter):
    output = re.split(delimeter, input_string)
    # print(f"{output}")
    return output


df["splits"] = df["data"].map(lambda x: split_string(input_string=x, delimeter=";|,"))
print(df.head(20))


def possible_game(guesses):
    temp_holding = {}
    power = 1
    print(guesses)
    # step through the guesses and validate of it is possible
    for guess in guesses:
        print(guess)
        # print(f"cube: {cube}")
        single_show = guess.split()
        colour = single_show[1]
        numb_cubes = int(single_show[0])
        # print(f"colour {colour} numb_cubes {numb_cubes}")
        if temp_holding.get(colour, -1) < numb_cubes:
            temp_holding.update({colour: numb_cubes})

    for k, v in temp_holding.items():
        power = power * v
    return power


df["power"] = df["splits"].map(lambda x: possible_game(guesses=x))
print(df[["game", "id_int", "power"]].head(20))

print(f'\n\nthe solution to the part a is: {df["power"].sum()}')
