import re
import os
import pandas as pd

pd.set_option("display.max_rows", 1001)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 2000)

path = "C:\\Users\\RoryAngus\\Documents\\CodeCommit\\data-science-tools\\archive\\2023-12-01_rory_aoc\\02"
os.chdir(path)
df = pd.read_csv(r"data.txt", sep="|", skiprows=0, header=None)  # , nrows=30)
print(f"df size: {len(df)}")
df.columns = ["data"]
print(df.head(20))

print("\n\n~~~~~~~~~~~~~part a~~~~~~~~~~~~\n\n")

game_limits = {"red": 12, "green": 13, "blue": 14}

# get the game into a column
df[["game", "guesses"]] = df["data"].str.split(":", n=1, expand=True)
print(df.head(20))


def split_string(input_string, delimeter):
    output = input_string.split(delimeter)
    # print(f"{output}")
    return output


df["splits"] = df["guesses"].map(lambda x: split_string(input_string=x, delimeter=";"))

df["id_int"] = df["game"].str.extract("(\d+)").astype(int)


def possible_game(guesses, game_limits=game_limits):
    # step through the guesses and validate of it is possible
    for guess in guesses:
        print(guess)
        shown_cubes = guess.split(",")
        for cube in shown_cubes:
            print(f"cube: {cube}")
            single_show = cube.split()
            colour = single_show[1]
            numb_cubes = int(single_show[0])
            print(f"colour {colour} numb_cubes {numb_cubes}")
            if numb_cubes > game_limits.get(colour):
                return False
    return True


df["game_possible"] = df["splits"].map(
    lambda x: possible_game(guesses=x, game_limits=game_limits)
)
print(df[["game", "id_int", "game_possible"]].head(20))

print(
    f'\n\nthe solution to the part a is: {df.loc[df["game_possible"]]["id_int"].sum()}'
)
