# with open("data.txt") as f:
#     lines = f.readlines()
# print(f"lines: {len(lines)}")
import os
import pandas as pd

path = "C:\\Users\\RoryAngus\\Documents\\CodeCommit\\data-science-tools\\archive\\2023-12-01_rory_aoc\\01"
os.chdir(path)
df = pd.read_csv(r"data.txt", skiprows=0, header=None)

print(f"df size: {len(df)}")
df.columns = ["data"]
df["numbers_only"] = df["data"].str.replace("[a-zA-Z]", "")
df["first_num"] = df["numbers_only"].str.strip().str[0]
df["last_num"] = df["numbers_only"].str.strip().str[-1]
df["new_num"] = df["first_num"] + df["last_num"]
df["new_num_int"] = pd.to_numeric(df["new_num"], errors="coerce")
df
print(f'the sum of the numbers is: {df["new_num_int"].sum()}')
