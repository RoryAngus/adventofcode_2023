import re
import os
import pandas as pd

pd.set_option("display.max_rows", 1001)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

path = "C:\\Users\\RoryAngus\\Documents\\CodeCommit\\data-science-tools\\archive\\2023-12-01_rory_aoc\\0x"
os.chdir(path)
df = pd.read_csv(r"data.txt", skiprows=0, header=None)  # , nrows=20)
