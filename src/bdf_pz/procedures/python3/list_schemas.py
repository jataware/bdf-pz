import pandas as pd
from prettytable import PrettyTable

# construct table for printing
table = [["Name", "Fields"]]
for name, value in existing_schemas.items():
    table.append([name, ",".join(value.keys())])

# print table of registered datasets
t = PrettyTable(table[0])
t.add_rows(table[1:])
t