import pandas as pd

def get_row(rows, text):
    matches = list(filter(lambda row: row[1].rstrip("\n") == text, enumerate(rows)))
    # print(matches)

    if len(matches) == 0:
        raise Exception(f"header {text} could not be found")
    if len(matches) > 1:
        raise Exception(f"duplicate header {text} was found")

    return matches[0][0]



filename = "examples/data/mixed.csv"
with open(filename) as fh:
    rows = fh.readlines()

starting_row = get_row(rows, "Planet name,Distance (AU),Mass")
# print(starting_row) # 7

end_row = len(rows) - get_row(rows, "City 1,City 2,distance")
# print(end_row) # 4

df = pd.read_csv(filename, skiprows=starting_row, skipfooter=end_row, engine="python")
print(df)

