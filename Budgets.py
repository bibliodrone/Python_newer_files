import glob
import os

pfad = os.getcwd() + "\\FundMenus"
os.chdir(pfad)
read_files = glob.glob("*.txt")

with open("Budget_result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
