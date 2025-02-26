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
    nocache=True,
    verbose=False,
    processing_strategy="streaming",
    execution_strategy="sequential",
    optimizer_strategy="pareto",
    allow_code_synth={{ allow_code_synth }},
    allow_token_reduction={{ allow_token_reduction }},
)

iterable = output.run(config)

statistics = []
results = []
for data_record_collection in iterable:
    records = data_record_collection.data_records
    stats = data_record_collection.plan_stats
    statistics.append(stats)
    # data_obj['source'] = record.filename #TODO?
    results.extend([r.to_dict() for r in records])

results_df = pd.DataFrame(results)
results_df