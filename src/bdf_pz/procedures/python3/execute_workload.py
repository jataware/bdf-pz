if "dataset" not in locals():
    output = "{{ output_dataset }}"
else:
    output = dataset

policy_method = "{{ policy_method }}"

if policy_method == "min_cost":
    policy = pz.MinCost()
elif policy_method == "max_quality":
    policy = pz.MaxQuality()

config = pz.QueryProcessorConfig(
    policy=policy,
    cache=False,
    verbose=False,
    execution_strategy="sequential",
    optimizer_strategy="pareto",
    allow_code_synth={{ allow_code_synth }},
)

results = output.run(config)

results_df = results.to_df()
results_df