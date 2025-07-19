import numpy as np

str_stats = ""
try:
    t = results.execution_stats.total_execution_time
    cost = results.execution_stats.total_execution_cost
    str_stats += f"\nTotal plan time: {np.round(t,2)}s"
    str_stats += f"\nTotal plan cost: {np.round(cost,2)}$"
except Exception as e:
    print("Exception", e)
    print("No statistics available.")

str_stats