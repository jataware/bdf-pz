import pandas as pd
from prettytable import PrettyTable
import os 

# construct table for printing
table = [["Name", "Path", "N. Files"]]
for path, descriptor in registered_datasets.items():
    try:
        n_files = len(os.listdir(descriptor))
    except:
        n_files = "1"
    table.append([path, descriptor[0], n_files])

# print table of registered datasets
t = PrettyTable(table[0])
t.add_rows(table[1:])
t