import numpy as np

try:
    for id, plan in execution_stats.plan_stats.items():
        print(plan.plan_str)
        time = plan.total_plan_time
        cost = plan.total_plan_cost
        print(f"Total plan time: {np.round(time,2)}s")
        print(f"Total plan cost: {np.round(cost,2)}$")
except:
    print("No statistics available.")