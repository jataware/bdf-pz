import numpy as np

try:
    t = stats.total_plan_time
    cost = stats.total_plan_cost
    str_stats += f"\nTotal plan time: {np.round(t,2)}s"
    str_stats += f"\nTotal plan cost: {np.round(cost,2)}$"
except Exception as e:
    print("Exception", e)
    print("No statistics available.")

str_stats