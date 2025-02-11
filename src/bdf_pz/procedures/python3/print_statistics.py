import numpy as np

try:
    for id, plan in execution_stats.plan_stats.items():
        stats = plan.plan_str
        t = plan.total_plan_time
        cost = plan.total_plan_cost
        stats += f"\nTotal plan time: {np.round(t,2)}s"
        stats += f"\nTotal plan cost: {np.round(cost,2)}$"
except Exception as e:
    print("Exception", e)
    print("No statistics available.")

stats