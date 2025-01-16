if "dataset" not in locals():
    output = "{{ output_dataset }}"
else:
    output = dataset

policy_method = "{{ policy_method }}"

# optimization block
engine = pz.NoSentinelPipelinedSingleThreadExecution
if policy_method == "min_cost":
    policy = pz.MinCost()
elif policy_method == "max_quality":
    policy = pz.MaxQuality()
records, execution_stats  =  pz.Execute(output,
                        policy = policy,
                        nocache=True,
                        allow_code_synth={{ allow_code_synth }},
                        allow_token_reduction={{ allow_token_reduction }},
                        execution_engine=engine)

results = []
statistics = []

for record in records:
    data_obj = {}
    for name in output.schema.field_names():
        data_obj[name] = record.__getattr__(name)
    data_obj['source'] = record.filename
    results.append(data_obj)
    # results.append(record.as_dict())

results_df = pd.DataFrame(results)
results_df